import builtins as __builtin__
import dis
import gc
import logging
import os
import pathlib
import re
import sys
import tempfile
import warnings
from functools import partial
from inspect import (
    indentsize,
    iscode,
    isframe,
    isfunction,
    ismethod,
    istraceback,
)
from operator import attrgetter, itemgetter
from pickle import Unpickler, UnpicklingError
from types import (
    BuiltinMethodType,
    FunctionType,
    MethodType,
    ModuleType,
)
from typing import Optional, Union

from minspect._internal import _isinstance, _main_module, _module_map, _namespace
from minspect._internal import _locate_object as at
from minspect._internal import _proxy_helper as reference
from minspect.source import getmodule, getsource

try:
    import ctypes

    HAS_CTYPES = True
    # if using `pypy`, pythonapi is not found
    IS_PYPY = not hasattr(ctypes, "pythonapi")
except ImportError:
    HAS_CTYPES = False
    IS_PYPY = False



PartialType = type(partial(int, base=2))
SuperType = type(super(Exception, TypeError()))
ItemGetterType = type(itemgetter(0))
AttrGetterType = type(attrgetter("__repr__"))


def _create_typemap():
    import types

    d = dict(list(__builtin__.__dict__.items()) + list(types.__dict__.items())).items()
    for key, value in d:
        if getattr(value, "__module__", None) == "builtins" and type(value) is type:
            yield key, value
    return


_reverse_typemap = dict(_create_typemap())
_reverse_typemap.update(
    {
        "PartialType": PartialType,
        "SuperType": SuperType,
        "ItemGetterType": ItemGetterType,
        "AttrGetterType": AttrGetterType,
    }
)


def getname(obj, force=False, fqn=False): #XXX: throw(?) to raise error on fail?
    """Get the name of the object. for lambdas, get the name of the pointer."""
    if fqn: return '.'.join(_namespace(obj))
    module = getmodule(obj)
    if not module: # things like "None" and "1"
        if not force: return None
        return repr(obj)
    try:
        #XXX: 'wrong' for decorators and curried functions ?
        #       if obj.func_closure: ...use logic from getimportable, etc ?
        name = obj.__name__
        if name == '<lambda>':
            return getsource(obj).split('=',1)[0].strip()
        # handle some special cases
        if module.__name__ in ['builtins','__builtin__'] and name == 'ellipsis':
             name = 'EllipsisType'
        return name
    except AttributeError: #XXX: better to just throw AttributeError ?
        if not force: return None
        name = repr(obj)
        if name.startswith('<'): # or name.split('('):
            return None
        return name


def _outdent(lines, spaces=None, all=True): # noqa: A002
    """Outdent lines of code, accounting for docs and line continuations."""
    indent = indentsize(lines[0])
    if spaces is None or spaces > indent or spaces < 0:
        spaces = indent
    for i in range(len(lines) if all else 1):
        # FIXME: works... but shouldn't outdent 2nd+ lines of multiline doc
        _indent = indentsize(lines[i])
        _spaces = _indent if spaces > _indent else spaces
        lines[i] = lines[i][_spaces:]
    return lines


def outdent(code, spaces=None,*, all=True): # noqa
    """Outdent a block of code (default is to strip all leading whitespace)."""
    indent = indentsize(code)
    if spaces is None or spaces > indent or spaces < 0:
        spaces = indent
    # XXX: will this delete '\n' in some cases?
    if not all:
        return code[spaces:]
    return "\n".join(_outdent(code.split("\n"), spaces=spaces, all=all))


def _import_module(import_name, safe=False):
    try:
        if import_name.startswith("__runtime__."):
            return sys.modules[import_name]
        elif "." in import_name:
            items = import_name.split(".")
            module = ".".join(items[:-1])
            obj = items[-1]
            submodule = getattr(__import__(module, None, None, [obj]), obj)
            if isinstance(submodule, ModuleType | type):
                return submodule
            return __import__(import_name, None, None, [obj])
        else:
            return __import__(import_name)
    except (ImportError, AttributeError, KeyError):
        if safe:
            return None
        raise

def _is_builtin_module(module):
    if not hasattr(module, "__file__"):
        return True
    if module.__file__ is None:
        return False
    # If a module file name starts with prefix, it should be a builtin
    # module, so should always be pickled as a reference.
    names = ["base_prefix", "base_exec_prefix", "exec_prefix", "prefix", "real_prefix"]
    rp = os.path.realpath
    # See https://github.com/uqfoundation/dill/issues/566
    return (
        any(
            module.__file__.startswith(getattr(sys, name)) or rp(module.__file__).startswith(rp(getattr(sys, name)))
            for name in names
            if hasattr(sys, name)
        )
        or "site-packages" in module.__file__
    )


def _is_imported_module(module):
    return getattr(module, "__loader__", None) is not None or module in sys.modules.values()


TEMPDIR = pathlib.PurePath(tempfile.gettempdir())
__all__ = ["parent", "reference", "at", "parents", "children"]




def parent(obj, objtype, ignore=()):
    """Find the parent of obj that is of type objtype.

    >>> listiter = iter([4, 5, 6, 7])
    >>> obj = parent(listiter, list)
    >>> obj == [4, 5, 6, 7]  # actually 'is', but don't have handle any longer
    True

    NOTE: objtype can be a single type (e.g. int or list) or a tuple of types.

    WARNING: if obj is a sequence (e.g. list), may produce unexpected results.
    Parent finds *one* parent (e.g. the last member of the sequence).
    """
    depth = 1
    chain = parents(obj, objtype, depth, ignore)
    parent = chain.pop()
    if parent is obj:
        return None
    return parent


def parents(obj, objtype, depth=1, ignore=()) -> list:
    """Find the chain of referents for obj. Chain will end with obj.

    objtype: an object type or tuple of types to search for
    depth: search depth (e.g. depth=2 is 'grandparents')
    ignore: an object or tuple of objects to ignore in the search
    """
    edge_func = gc.get_referents  # looking for refs, not back_refs
    predicate = lambda x: isinstance(x, objtype)  # looking for parent type
    ignore = (ignore,) if not hasattr(ignore, "__len__") else ignore
    ignore = (id(obj) for obj in ignore)
    return find_chain(obj, predicate, edge_func, depth)[::-1]


def children(obj, objtype, depth=1, ignore=()) -> list:
    """Find the chain of referrers for obj. Chain will start with obj.

    objtype: an object type or tuple of types to search for
    depth: search depth (e.g. depth=2 is 'grandchildren')
    ignore: an object or tuple of objects to ignore in the search

    NOTE: a common thing to ignore is all globals, 'ignore=(globals(),)'

    NOTE: repeated calls may yield different results, as python stores
    the last value in the special variable '_'; thus, it is often good
    to execute something to replace '_' (e.g. >>> 1+1).
    """
    edge_func = gc.get_referrers  # looking for back_refs, not refs
    predicate = lambda x: isinstance(x, objtype)  # looking for child type
    ignore = (ignore,) if not hasattr(ignore, "__len__") else ignore
    ignore = (id(obj) for obj in ignore)
    return find_chain(obj, predicate, edge_func, depth, ignore)


# more generic helper function (cut-n-paste from objgraph)
# Source at http://mg.pov.lt/objgraph/
# Copyright (c) 2008-2010 Marius Gedminas <marius@pov.lt>
# Copyright (c) 2010 Stefano Rivera <stefano@rivera.za.net>
# Released under the MIT licence (see objgraph/objgrah.py)


def find_chain(obj, predicate, edge_func, max_depth=20, extra_ignore=()):
    queue = [obj]
    depth = {id(obj): 0}
    parent = {id(obj): None}
    ignore = set(extra_ignore)
    ignore.add(id(extra_ignore))
    ignore.add(id(queue))
    ignore.add(id(depth))
    ignore.add(id(parent))
    ignore.add(id(ignore))
    ignore.add(id(sys._getframe()))  # this function
    ignore.add(id(sys._getframe(1)))  # find_chain/find_backref_chain, likely
    gc.collect()
    while queue:
        target = queue.pop(0)
        if predicate(target):
            chain = [target]
            while parent[id(target)] is not None:
                target = parent[id(target)]
                chain.append(target)
            return chain
        tdepth = depth[id(target)]
        if tdepth < max_depth:
            referrers = edge_func(target)
            ignore.add(id(referrers))
            for source in referrers:
                if id(source) in ignore:
                    continue
                if id(source) not in depth:
                    depth[id(source)] = tdepth + 1
                    parent[id(source)] = target
                    queue.append(source)
    return [obj]  # not found


IMPORTED_AS_TYPES = (ModuleType, type, FunctionType, MethodType, BuiltinMethodType)
if "PyCapsuleType" in _reverse_typemap:
    IMPORTED_AS_TYPES += (_reverse_typemap["PyCapsuleType"],)
IMPORTED_AS_MODULES = (
    "ctypes",
    "typing",
    "subprocess",
    "threading",
    r"concurrent\.futures(\.\w+)?",
    r"multiprocessing(\.\w+)?",
)
IMPORTED_AS_MODULES = tuple(re.compile(x) for x in IMPORTED_AS_MODULES)


def _lookup_module(modmap, name, obj, main_module):
    """Lookup name or id of obj if module is imported."""
    for modobj, modname in modmap.by_name[name]:
        if modobj is obj and sys.modules[modname] is not main_module:
            return modname, name
    __module__ = getattr(obj, "__module__", None)
    if isinstance(obj, IMPORTED_AS_TYPES) or (
        __module__ is not None and any(regex.fullmatch(__module__) for regex in IMPORTED_AS_MODULES)
    ):
        for modobj, objname, modname in modmap.by_id[id(obj)]:
            if sys.modules[modname] is not main_module:
                return modname, objname
    return None, None


def _stash_modules(main_module):
    modmap = _module_map()
    newmod = ModuleType(main_module.__name__)

    imported = []
    imported_as = []
    imported_top_level = []  # keep separated for backward compatibility
    original = {}
    for name, obj in main_module.__dict__.items():
        if obj is main_module:
            original[name] = newmod  # self-reference
        elif obj is main_module.__dict__:
            original[name] = newmod.__dict__
        # Avoid incorrectly matching a singleton value in another package (ex.: __doc__).
        elif (
            any(obj is singleton for singleton in (None, False, True))
            or isinstance(obj, ModuleType)
            and _is_builtin_module(obj)
        ):  # always saved by ref
            original[name] = obj
        else:
            source_module, objname = _lookup_module(modmap, name, obj, main_module)
            if source_module is not None:
                if objname == name:
                    imported.append((source_module, name))
                else:
                    imported_as.append((source_module, objname, name))
            else:
                try:
                    imported_top_level.append((modmap.top_level[id(obj)], name))
                except KeyError:
                    original[name] = obj

    if len(original) < len(main_module.__dict__):
        newmod.__dict__.update(original)
        newmod.__mbodi_imported = imported
        newmod.__mbodi_imported_as = imported_as
        newmod.__mbodi_imported_top_level = imported_top_level
        if getattr(newmod, "__loader__", None) is None and _is_imported_module(main_module):
            # Trick _is_imported_module() to force saving as an imported module.
            newmod.__loader__ = True  # will be discarded by save_module()
        return newmod

    return main_module


def _restore_modules(unpickler, main_module):
    try:
        for modname, name in main_module.__dict__.pop("__mbodi_imported"):
            main_module.__dict__[name] = unpickler.find_class(modname, name)
        for modname, objname, name in main_module.__dict__.pop("__mbodi_imported_as"):
            main_module.__dict__[name] = unpickler.find_class(modname, objname)
        for modname, name in main_module.__dict__.pop("__mbodi_imported_top_level"):
            main_module.__dict__[name] = __import__(modname)
    except KeyError:
        pass



def dump_module(
    filename: str | os.PathLike = None,
    module: ModuleType | str | None = None,
    refimported: bool = False,
    **kwds,
) -> None:
    """Pickle the current state of :py:mod:`__main__` or another module to a file.

    Save the contents of :py:mod:`__main__` (e.g. from an interactive
    interpreter session), an imported module, or a module-type object (e.g.
    built with :py:class:`~types.ModuleType`), to a file. The pickled
    module can then be restored with the function :py:func:`load_module`.

    Args:
        filename: a path-like object or a writable stream. If `None`
            (the default), write to a named file in a temporary directory.
        module: a module object or the name of an importable module. If `None`
            (the default), :py:mod:`__main__` is saved.
        refimported: if `True`, all objects identified as having been imported
            into the module's namespace are saved by reference. *Note:* this is
            similar but independent from ``mbodi.settings[`byref`]``, as
            ``refimported`` refers to virtually all imported objects, while
            ``byref`` only affects select objects.
        **kwds: extra keyword arguments passed to :py:class:`Pickler()`.

    Raises:
       :py:exc:`PicklingError`: if pickling fails.

    Examples:

        - Save current interpreter session state:

          >>> import mbodi
          >>> squared = lambda x: x * x
          >>> mbodi.dump_module()  # save state of __main__ to /tmp/session.pkl

        - Save the state of an imported/importable module:

          >>> import mbodi
          >>> import pox
          >>> pox.plus_one = lambda x: x + 1
          >>> mbodi.dump_module("pox_session.pkl", module=pox)

        - Save the state of a non-importable, module-type object:

          >>> import mbodi
          >>> from types import ModuleType
          >>> foo = ModuleType("foo")
          >>> foo.values = [1, 2, 3]
          >>> import math
          >>> foo.sin = math.sin
          >>> mbodi.dump_module("foo_session.pkl", module=foo, refimported=True)

        - Restore the state of the saved modules:

          >>> import mbodi
          >>> mbodi.load_module()
          >>> squared(2)
          4
          >>> pox = mbodi.load_module("pox_session.pkl")
          >>> pox.plus_one(1)
          2
          >>> foo = mbodi.load_module("foo_session.pkl")
          >>> [foo.sin(x) for x in foo.values]
          [0.8414709848078965, 0.9092974268256817, 0.1411200080598672]

        - Use `refimported` to save imported objects by reference:

          >>> import mbodi
          >>> from html.entities import html5
          >>> type(html5), len(html5)
          (dict, 2231)
          >>> import io
          >>> buf = io.BytesIO()
          >>> mbodi.dump_module(buf)  # saves __main__, with html5 saved by value
          >>> len(buf.getvalue())  # pickle size in bytes
          71665
          >>> buf = io.BytesIO()
          >>> mbodi.dump_module(buf, refimported=True)  # html5 saved by reference
          >>> len(buf.getvalue())
          438

    *Changed in version 0.3.6:* Function ``dump_session()`` was renamed to
    ``dump_module()``.  Parameters ``main`` and ``byref`` were renamed to
    ``module`` and ``refimported``, respectively.

    Note:
        Currently, ``mbodi.settings['byref']`` and ``mbodi.settings['recurse']``
        don't apply to this function.
    """
    for old_par, par in [("main", "module"), ("byref", "refimported")]:
        if old_par in kwds:
            message = "The argument %r has been renamed %r" % (old_par, par)
            if old_par == "byref":
                message += " to distinguish it from mbodi.settings['byref']"
            warnings.warn(message + ".", PendingDeprecationWarning)
            if locals()[par]:  # the defaults are None and False
                raise TypeError("both %r and %r arguments were used" % (par, old_par))
    refimported = kwds.pop("byref", refimported)
    module = kwds.pop("main", module)

    protocol = "pickle"
    main = module
    if main is None:
        main = _main_module
    elif isinstance(main, str):
        main = _import_module(main)
    if not isinstance(main, ModuleType):
        raise TypeError("%r is not a module" % main)
    if hasattr(filename, "write"):
        file = filename
    else:
        if filename is None:
            filename = str(TEMPDIR / "session.pkl")
        file = open(filename, "wb")
    if file is not filename:  # if newly opened file
        file.close()
    return


# Backward compatibility.
def dump_session(filename=None, main=None, byref=False, **kwds):
    warnings.warn("dump_session() has been renamed dump_module()", PendingDeprecationWarning)
    dump_module(filename, module=main, refimported=byref, **kwds)


dump_session.__doc__ = dump_module.__doc__


class _PeekableReader:
    """Lightweight stream wrapper that implements peek()."""

    def __init__(self, stream):
        self.stream = stream

    def read(self, n):
        return self.stream.read(n)

    def readline(self):
        return self.stream.readline()

    def tell(self):
        return self.stream.tell()

    def close(self):
        return self.stream.close()

    def peek(self, n):
        stream = self.stream
        try:
            if hasattr(stream, "flush"):
                stream.flush()
            position = stream.tell()
            stream.seek(position)  # assert seek() works before reading
            chunk = stream.read(n)
            stream.seek(position)
            return chunk
        except (AttributeError, OSError):
            raise NotImplementedError("stream is not peekable: %r", stream) from None


def _make_peekable(stream):
    """Return stream as an object with a peek() method."""
    import io

    if hasattr(stream, "peek"):
        return stream
    if not (hasattr(stream, "tell") and hasattr(stream, "seek")):
        try:
            return io.BufferedReader(stream)
        except Exception:
            logging.log(logging.DEBUG, "stream is not peekable: %r", stream)
            pass
    return _PeekableReader(stream)


def _identify_module(file, main=None):
    """identify the name of the module stored in the given file-type object"""
    from pickletools import genops

    UNICODE = {"UNICODE", "BINUNICODE", "SHORT_BINUNICODE"}
    found_import = False
    try:
        for opcode, arg, pos in genops(file.peek(256)):
            if not found_import:
                if opcode.name in ("GLOBAL", "SHORT_BINUNICODE") and arg.endswith("_import_module"):
                    found_import = True
            else:
                if opcode.name in UNICODE:
                    return arg
        else:
            raise UnpicklingError("reached STOP without finding main module")
    except (NotImplementedError, ValueError) as error:
        # ValueError occours when the end of the chunk is reached (without a STOP).
        if isinstance(error, NotImplementedError) and main is not None:
            # file is not peekable, but we have main.
            return None
        raise UnpicklingError("unable to identify main module") from error


def load_module(
    filename: Union[str, os.PathLike] = None, module: Optional[Union[ModuleType, str]] = None, **kwds
) -> Optional[ModuleType]:
    """Update the selected module (default is :py:mod:`__main__`) with the state saved at ``filename``.

    Restore a module to the state saved with :py:func:`dump_module`. The
    saved module can be :py:mod:`__main__` (e.g. an interpreter session),
    an imported module, or a module-type object (e.g. created with
    :py:class:`~types.ModuleType`).

    When restoring the state of a non-importable module-type object, the
    current instance of this module may be passed as the argument ``main``.
    Otherwise, a new instance is created with :py:class:`~types.ModuleType`
    and returned.

    Args:
        filename: a path-like object or a readable stream. If `None`
            (the default), read from a named file in a temporary directory.
        module: a module object or the name of an importable module;
            the module name and kind (i.e. imported or non-imported) must
            match the name and kind of the module stored at ``filename``.
        **kwds: extra keyword arguments passed to :py:class:`Unpickler()`.

    Raises:
        :py:exc:`UnpicklingError`: if unpickling fails.
        :py:exc:`ValueError`: if the argument ``main`` and module saved
            at ``filename`` are incompatible.

    Returns:
        A module object, if the saved module is not :py:mod:`__main__` or
        a module instance wasn't provided with the argument ``main``.

    Examples:

        - Save the state of some modules:

          >>> import mbodi
          >>> squared = lambda x: x * x
          >>> mbodi.dump_module()  # save state of __main__ to /tmp/session.pkl
          >>>
          >>> import pox  # an imported module
          >>> pox.plus_one = lambda x: x + 1
          >>> mbodi.dump_module("pox_session.pkl", module=pox)
          >>>
          >>> from types import ModuleType
          >>> foo = ModuleType("foo")  # a module-type object
          >>> foo.values = [1, 2, 3]
          >>> import math
          >>> foo.sin = math.sin
          >>> mbodi.dump_module("foo_session.pkl", module=foo, refimported=True)

        - Restore the state of the interpreter:

          >>> import mbodi
          >>> mbodi.load_module()  # updates __main__ from /tmp/session.pkl
          >>> squared(2)
          4

        - Load the saved state of an importable module:

          >>> import mbodi
          >>> pox = mbodi.load_module("pox_session.pkl")
          >>> pox.plus_one(1)
          2
          >>> import sys
          >>> pox in sys.modules.values()
          True

        - Load the saved state of a non-importable module-type object:

          >>> import mbodi
          >>> foo = mbodi.load_module("foo_session.pkl")
          >>> [foo.sin(x) for x in foo.values]
          [0.8414709848078965, 0.9092974268256817, 0.1411200080598672]
          >>> import math
          >>> foo.sin is math.sin  # foo.sin was saved by reference
          True
          >>> import sys
          >>> foo in sys.modules.values()
          False

        - Update the state of a non-importable module-type object:

          >>> import mbodi
          >>> from types import ModuleType
          >>> foo = ModuleType("foo")
          >>> foo.values = ["a", "b"]
          >>> foo.sin = lambda x: x * x
          >>> mbodi.load_module("foo_session.pkl", module=foo)
          >>> [foo.sin(x) for x in foo.values]
          [0.8414709848078965, 0.9092974268256817, 0.1411200080598672]

    *Changed in version 0.3.6:* Function ``load_session()`` was renamed to
    ``load_module()``. Parameter ``main`` was renamed to ``module``.

    See also:
        :py:func:`load_module_asdict` to load the contents of module saved
        with :py:func:`dump_module` into a dictionary.
    """
    if "main" in kwds:
        warnings.warn("The argument 'main' has been renamed 'module'.", PendingDeprecationWarning)
        if module is not None:
            raise TypeError("both 'module' and 'main' arguments were used")
        module = kwds.pop("main")
    main = module
    if hasattr(filename, "read"):
        file = filename
    else:
        if filename is None:
            filename = str(TEMPDIR / "session.pkl")
        file = open(filename, "rb")
    try:
        file = _make_peekable(file)
        # FIXME: mbodi.settings are disabled
        unpickler = Unpickler(file, **kwds)
        unpickler._session = True

        # Resolve unpickler._main
        pickle_main = _identify_module(file, main)
        if main is None and pickle_main is not None:
            main = pickle_main
        if isinstance(main, str):
            if main.startswith("__runtime__."):
                # Create runtime module to load the session into.
                main = ModuleType(main.partition(".")[-1])
            else:
                main = _import_module(main)
        if main is not None:
            if not isinstance(main, ModuleType):
                raise TypeError("%r is not a module" % main)
            unpickler._main = main
        else:
            main = unpickler._main

        # Check against the pickle's main.
        is_main_imported = _is_imported_module(main)
        if pickle_main is not None:
            is_runtime_mod = pickle_main.startswith("__runtime__.")
            if is_runtime_mod:
                pickle_main = pickle_main.partition(".")[-1]
            error_msg = "can't update{} module{} %r with the saved state of{} module{} %r"
            if is_runtime_mod and is_main_imported:
                raise ValueError(error_msg.format(" imported", "", "", "-type object") % (main.__name__, pickle_main))
            if not is_runtime_mod and not is_main_imported:
                raise ValueError(error_msg.format("", "-type object", " imported", "") % (pickle_main, main.__name__))
            if main.__name__ != pickle_main:
                raise ValueError(error_msg.format("", "", "", "") % (main.__name__, pickle_main))

        # This is for find_class() to be able to locate it.
        if not is_main_imported:
            runtime_main = "__runtime__.%s" % main.__name__
            sys.modules[runtime_main] = main

        loaded = unpickler.load()
    finally:
        if not hasattr(filename, "read"):  # if newly opened file
            file.close()
        try:
            del sys.modules[runtime_main]
        except (KeyError, NameError):
            pass
    assert loaded is main
    _restore_modules(unpickler, main)
    if main is _main_module or main is module:
        return None
    else:
        return main

def _enclose(object, alias=""):  # FIXME: needs alias to hold returned object
    """create a function enclosure around the source of some object"""
    # XXX: dummy and stub should append a random string
    dummy = "__this_is_a_big_dummy_enclosing_function__"
    stub = "__this_is_a_stub_variable__"
    code = "def %s():\n" % dummy
    code += indent(getsource(object, alias=stub, lstrip=True, force=True))
    code += indent("return %s\n" % stub)
    if alias:
        code += "%s = " % alias
    code += "%s(); del %s\n" % (dummy, dummy)
    # code += "globals().pop('%s',lambda :None)()\n" % dummy
    return code


def dumpsource(object, alias="", new=False, enclose=True):
    """'dump to source', where the code includes a pickled object.

    If new=True and object is a class instance, then create a new
    instance using the unpacked class source code. If enclose, then
    create the object inside a function enclosure (thus minimizing
    any global namespace pollution).
    """
    from mlink import dumps

    pik = repr(dumps(object))
    code = "import mbodi\n"
    if enclose:
        stub = "__this_is_a_stub_variable__"  # XXX: *must* be same _enclose.stub
        pre = f"{stub} = "
        new = False  # FIXME: new=True doesn't work with enclose=True
    else:
        stub = alias
        pre = f"{stub} = " if alias else alias

    # if a 'new' instance is not needed, then just dump and load
    if not new or not _isinstance(object):
        code += pre + f"mlink.loads({pik})\n"
    else:  # XXX: other cases where source code is needed???
        code += getsource(object.__class__, alias="", lstrip=True, force=True)
        mod = repr(object.__module__)  # should have a module (no builtins here)
        code += pre + f'mlink.loads({pik}.replace(b{mod},bytes(__name__,"UTF-8")))\n'
    # code += 'del %s' % object.__class__.__name__ #NOTE: kills any existing!

    if enclose:
        # generation of the 'enclosure'
        dummy = "__this_is_a_big_dummy_object__"
        dummy = _enclose(dummy, alias=alias)
        # hack to replace the 'dummy' with the 'real' code
        dummy = dummy.split("\n")
        code = dummy[0] + "\n" + indent(code) + "\n".join(dummy[-3:])

    return code  # XXX: better 'dumpsourcelines', returning list of lines?


# Backward compatibility.
def load_session(filename=None, main=None, **kwds):
    warnings.warn("load_session() has been renamed load_module().", PendingDeprecationWarning)
    load_module(filename, module=main, **kwds)


load_session.__doc__ = load_module.__doc__


def load_module_asdict(filename: Union[str, os.PathLike] = None, update: bool = False, **kwds) -> dict:
    """Load the contents of a saved module into a dictionary.

    ``load_module_asdict()`` is the near-equivalent of::

        lambda filename: vars(mbodi.load_module(filename)).copy()

    however, does not alter the original module. Also, the path of
    the loaded module is stored in the ``__session__`` attribute.

    Args:
        filename: a path-like object or a readable stream. If `None`
            (the default), read from a named file in a temporary directory.
        update: if `True`, initialize the dictionary with the current state
            of the module prior to loading the state stored at filename.
        **kwds: extra keyword arguments passed to :py:class:`Unpickler()`

    Raises:
        :py:exc:`UnpicklingError`: if unpickling fails

    Returns:
        A copy of the restored module's dictionary.

    Note:
        If ``update`` is True, the corresponding module may first be imported
        into the current namespace before the saved state is loaded from
        filename to the dictionary. Note that any module that is imported into
        the current namespace as a side-effect of using ``update`` will not be
        modified by loading the saved module in filename to a dictionary.

    Example:
        >>> import mbodi
        >>> alist = [1, 2, 3]
        >>> anum = 42
        >>> mbodi.dump_module()
        >>> anum = 0
        >>> new_var = "spam"
        >>> main = mbodi.load_module_asdict()
        >>> main["__name__"], main["__session__"]
        ('__main__', '/tmp/session.pkl')
        >>> main is globals()  # loaded objects don't reference globals
        False
        >>> main["alist"] == alist
        True
        >>> main["alist"] is alist  # was saved by value
        False
        >>> main["anum"] == anum  # changed after the session was saved
        False
        >>> new_var in main  # would be True if the option 'update' was set
        False
    """
    if "module" in kwds:
        raise TypeError("'module' is an invalid keyword argument for load_module_asdict()")
    if hasattr(filename, "read"):
        file = filename
    else:
        if filename is None:
            filename = str(TEMPDIR / "session.pkl")
        file = open(filename, "rb")
    try:
        file = _make_peekable(file)
        main_name = _identify_module(file)
        old_main = sys.modules.get(main_name)
        main = ModuleType(main_name)
        if update:
            if old_main is None:
                old_main = _import_module(main_name)
            main.__dict__.update(old_main.__dict__)
        else:
            main.__builtins__ = __builtin__
        sys.modules[main_name] = main
        load_module(file, **kwds)
    finally:
        if not hasattr(filename, "read"):  # if newly opened file
            file.close()
        try:
            if old_main is None:
                del sys.modules[main_name]
            else:
                sys.modules[main_name] = old_main
        except NameError:  # failed before setting old_main
            pass
    main.__session__ = str(filename)
    return main.__dict__

def code(func):
    """get the code object for the given function or method"""
    if ismethod(func):
        func = func.__func__
    if isfunction(func):
        func = func.__code__
    if istraceback(func):
        func = func.tb_frame
    if isframe(func):
        func = func.f_code
    if iscode(func):
        return func
    return None

def nestedglobals(func, recurse=True):
    """get the names of any globals found within func"""
    func = code(func)
    if func is None:
        return list()
    import sys
    from .temp import capture

    CAN_NULL = sys.hexversion >= 0x30B00A7  # NULL may be prepended >= 3.11a7
    names = set()
    with capture("stdout") as out:
        dis.dis(func)  # XXX: dis.dis(None) disassembles last traceback
    for line in out.getvalue().splitlines():
        if "_GLOBAL" in line:
            name = line.split("(")[-1].split(")")[0]
            if CAN_NULL:
                names.add(name.replace("NULL + ", "").replace(" + NULL", ""))
            else:
                names.add(name)
    for co in getattr(func, "co_consts", tuple()):
        if co and recurse and iscode(co):
            names.update(nestedglobals(co, recurse=True))
    return list(names)

def referredglobals(func, recurse=True, builtin=False):
    """get the names of objects in the global scope referred to by func"""
    return globalvars(func, recurse, builtin).keys()


def globalvars(func, recurse=True, builtin=False):
    """get objects defined in global scope that are referred to by func

    return a dict of {name:object}"""
    if ismethod(func):
        func = func.__func__
    if isfunction(func):
        globs = vars(getmodule(sum)).copy() if builtin else {}
        # get references from within closure
        orig_func, func = func, set()
        for obj in orig_func.__closure__ or {}:
            try:
                cell_contents = obj.cell_contents
            except ValueError:  # cell is empty
                pass
            else:
                _vars = globalvars(cell_contents, recurse, builtin) or {}
                func.update(_vars)  # XXX: (above) be wary of infinte recursion?
                globs.update(_vars)
        # get globals
        globs.update(orig_func.__globals__ or {})
        # get names of references
        if not recurse:
            func.update(orig_func.__code__.co_names)
        else:
            func.update(nestedglobals(orig_func.__code__))
            # find globals for all entries of func
            for key in func.copy():  # XXX: unnecessary...?
                nested_func = globs.get(key)
                if nested_func is orig_func:
                    # func.remove(key) if key in func else None
                    continue  # XXX: globalvars(func, False)?
                func.update(globalvars(nested_func, True, builtin))
    elif iscode(func):
        globs = vars(getmodule(sum)).copy() if builtin else {}
        # globs.update(globals())
        if not recurse:
            func = func.co_names  # get names
        else:
            orig_func = func.co_name  # to stop infinite recursion
            func = set(nestedglobals(func))
            # find globals for all entries of func
            for key in func.copy():  # XXX: unnecessary...?
                if key is orig_func:
                    # func.remove(key) if key in func else None
                    continue  # XXX: globalvars(func, False)?
                nested_func = globs.get(key)
                func.update(globalvars(nested_func, True, builtin))
    else:
        return {}
    # NOTE: if name not in __globals__, then we skip it...
    return dict((name, globs[name]) for name in func if name in globs)


def varnames(func):
    """get names of variables defined by func

    returns a tuple (local vars, local vars referrenced by nested functions)"""
    func = code(func)
    if not iscode(func):
        return ()  # XXX: better ((),())? or None?
    return func.co_varnames, func.co_cellvars
