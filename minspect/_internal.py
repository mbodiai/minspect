import contextlib
import gc
import sys
from ast import AST
from inspect import getmodule, getsource, ismodule
from types import ModuleType, SimpleNamespace
from typing import Callable, dataclass_transform

from typing_extensions import Protocol, TypedDict

import __main__ as _main_module
from minspect.source import isintypes  # noqa

try:
    import ctypes

    HAS_CTYPES = True
    # if using `pypy`, pythonapi is not found
    IS_PYPY = not hasattr(ctypes, "pythonapi")
except ImportError:
    HAS_CTYPES = False
    IS_PYPY = False

@dataclass_transform()
class ModuleMap(TypedDict, total=False):
    by_name: dict[str, list[tuple[object, str]]]
    by_id: dict[int, list[tuple[object, str, str]]]
    top_level: dict[int, str]

class Context(TypedDict, total=False):
    ancestor_instructions: list[str]
    instruction: str
    notes: str

class SharedState(TypedDict, total=False):
    instruction: str
    shared_ctx: Context
    

class Tree(TypedDict, total=False):
    by_name: dict[str, list[tuple[object, str]]]
    by_id: dict[int, list[tuple[object, str, str]]]
    top_level: dict[int, str]
    modules: dict[str, ModuleType]
    classes: dict[str, type]
    functions: dict[str, Callable]
    objects: dict[str, object]
    ast: dict[str, AST]
    source: dict[str, str]
    shared_state: SharedState
    children_ctx: dict[str, Context]
    


def modulemap():
    """Get map of imported modules."""
    from collections import defaultdict

    modmap = ModuleMap(
        by_name=defaultdict(list),
        by_id=defaultdict(list),
        top_level={},
    )
    for modname, module in sys.modules.items():
        if modname in ("__main__", "__mp_main__") or not isinstance(module, ModuleType):
            continue
        if "." not in modname:
            modmap.top_level[id(module)] = modname
        for objname, modobj in module.__dict__.items():
            modmap.by_name[objname].append((modobj, modname))
            modmap.by_id[id(modobj)].append((modobj, objname, modname))
    return modmap


def astdict(obj):
    """Get dictionary of AST nodes for the given object."""
    import ast

    return {node.__class__.__name__: node for node in ast.walk(ast.parse(getsource(obj)))}

@contextlib.contextmanager
def capture(stream="stdout"):
    """Builds a context that temporarily replaces the given stream name.

    >>> with capture("stdout") as out:
    ...     print("foo!")
    >>> print(out.getvalue())
    foo!

    """
    import sys
    from io import StringIO

    orig = getattr(sys, stream)
    setattr(sys, stream, StringIO())
    try:
        yield getattr(sys, stream)
    finally:
        setattr(sys, stream, orig)


def namespaces(obj):
    r"""Return namespace hierarchy (as a list of names) for the given object.
    
    For an instance, find the class hierarchy.

    For example:

    >>> from functools import partial
    >>> p = partial(int, base=2)
    >>> _namespace(p)
    [\'functools\', \'partial\']
    """
    from minspect.source import getname
    # mostly for functions and modules and such
    # FIXME: 'wrong' for decorators and curried functions
    with contextlib.suppress(AttributeError, TypeError, NameError):
        module = qual = str(getmodule(obj)).split()[1].strip(">").strip('"').strip("'")
        qual = qual.split(".")
        if ismodule(obj):
            return qual
        # get name of a lambda, function, etc
        name = getname(obj) or obj.__name__  # failing, raise AttributeError
        # check special cases (NoneType, ...)
        if module in ["builtins", "__builtin__"] and isintypes(name):
            return ["types"] + [name]
        return qual + [name]  # XXX: can be wrong for some aliased objects

    # special case: numpy.inf and numpy.nan (we don't want them as floats)
    if str(obj) in ["inf", "nan", "Inf", "NaN"]:  # is more, but are they needed?
        return ["numpy"] + [str(obj)]
    # mostly for classes and class instances and such
    module = getattr(obj.__class__, "__module__", None)
    qual = str(obj.__class__)
    with contextlib.suppress(ValueError):
        qual = qual[qual.index("'") + 1 : -2]
    qual = qual.split(".")
    if module in ["builtins", "__builtin__"]:
        # check special cases (NoneType, Ellipsis, ...)
        if qual[-1] == "ellipsis":
            qual[-1] = "EllipsisType"
        if isintypes(qual[-1]):
            module = "types"  # XXX: BuiltinFunctionType
        qual = [module] + qual
    return qual

def getimport(obj, alias="", verify=True, builtin=False, enclosing=False):
    """Get the likely import string for the given object.

    obj is the object to inspect
    If verify=True, then test the import string before returning it.
    If builtin=True, then force an import for builtins where possible.
    If enclosing=True, get the import for the outermost enclosing callable.
    If alias is provided, then rename the object on import.
    """
    if enclosing:
        from minspect.source import _getimport, outermost

        _obj = outermost(obj)
        obj = _obj if _obj else obj
    # get the namespace
    qual = namespaces(obj)
    head = ".".join(qual[:-1])
    tail = qual[-1]
    # for named things... with a nice repr #XXX: move into _namespace?
    try:  # look for '<...>' and be mindful it might be in lists, dicts, etc...
        name = repr(obj).split("<", 1)[1].split(">", 1)[1]
        name = None  # we have a 'object'-style repr
    except Exception:  # it's probably something 'importable'
        name = repr(obj) if head in ["builtins", "__builtin__"] else repr(obj).split("(")[0]
    if name:  # try using name instead of tail
        try:
            return _getimport(head, name, alias, verify, builtin)
        except ImportError:
            pass
        except SyntaxError:
            if head in ["builtins", "__builtin__"]:
                _alias = f"{alias} = " if alias else ""
                if alias == name:
                    _alias = ""
                return _alias + f"{name}\n"

    try:
        return _getimport(head, tail, alias, verify, builtin)
    except ImportError:
        raise  # could do some checking against obj
    except SyntaxError:
        if head in ["builtins", "__builtin__"]:
            _alias = f"{alias} = " if alias else ""
            if alias == tail:
                _alias = ""
            return _alias + f"{tail}\n"
        raise  # could do some checking against o


def _proxy_helper(obj):  # a dead proxy returns a reference to None
    """Get memory address of proxy's reference object."""
    _repr = repr(obj)
    try:
        _str = str(obj)
    except ReferenceError:  # it's a dead proxy
        return id(None)
    if _str == _repr:
        return id(obj)  # it's a repr
    try:  # either way, it's a proxy from here
        address = int(_str.rstrip(">").split(" at ")[-1], base=16)
    except ValueError as e:
        if not IS_PYPY:
            address = int(_repr.rstrip(">").split(" at ")[-1], base=16)
        else:
            objects = iter(gc.get_objects())
            for _obj in objects:
                if repr(_obj) == _str:
                    return id(_obj)
            # all bad below... nothing found so throw ReferenceError
            msg = f"Cannot reference object for proxy at '{id(obj)}'"
            raise ReferenceError(msg) from e
    return address


def _locate_object(address, module=None):
    """Get object located at the given memory address (inverse of id(obj))."""
    special = [None, True, False]  # XXX: more...?
    for obj in special:
        if address == id(obj):
            return obj
    objects = iter(module.__dict__.values()) if module else iter(gc.get_objects())
    for obj in objects:
        if address == id(obj):
            return obj
    # all bad below... nothing found so throw ReferenceError or TypeError
    try:
        address = hex(address)
    except TypeError as e:
        raise TypeError(f"'{str(address)}' is not a valid memory address") from e
    raise ReferenceError(f"Cannot reference object at '{address}'")


