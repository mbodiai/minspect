import dis
import re
import sys
from inspect import (
    findsource,
    getblock,
    getmodule,
    indentsize,
    isclass,
    iscode,
    isframe,
    isfunction,
    ismethod,
    ismodule,
    istraceback,
)
from pickle import dumps
from tokenize import TokenError
from types import ModuleType

from minspect._internal import _namespace, getimport


def importmodule(import_name: str, safe=False):
    try:
        if import_name.startswith("__runtime__."):
            return sys.modules[import_name]
        if "." in import_name:
            items = import_name.split(".")
            module = ".".join(items[:-1])
            obj = items[-1]
            submodule = getattr(__import__(module, None, None, [obj]), obj)
            if isinstance(submodule, ModuleType | type):
                return submodule
            return __import__(import_name, None, None, [obj])

        return __import__(import_name)
    except (ImportError, AttributeError, KeyError):
        if safe:
            return None
        raise


def _getimport(head, tail, alias="", verify=True, builtin=False):
    """Helper to build a likely import string from head and tail of namespace.

    ('head','tail') are used in the following context: "from head import tail".

    If verify=True, then test the import string before returning it.
    If builtin=True, then force an import for builtins where possible.
    If alias is provided, then rename the obj on import.
    """
    # special handling for a few common types
    if tail in ["Ellipsis", "NotImplemented"] and head in ["types"]:
        head = len.__module__
    elif tail in ["None"] and head in ["types"]:
        _alias = f"{alias} = " if alias else ""
        if alias == tail:
            _alias = ""
        return _alias + f"{tail}\n"

    if head in ["builtins", "__builtin__"]:
        # special cases (NoneType, Ellipsis, ...) #XXX: BuiltinFunctionType
        if tail == "ellipsis":
            tail = "EllipsisType"
        if isintypes(tail):
            head = "types"
        elif not builtin:
            _alias = f"{alias} = " if alias else ""
            if alias == tail:
                _alias = ""
            return _alias + f"{tail}\n"
        else:
            pass  # handle builtins below
    # get likely import string
    _str = f"import {tail}" if not head else f"from {head} import {tail}"
    _alias = f" as {alias}\n" if alias else "\n"
    if alias == tail:
        _alias = "\n"
    _str += _alias
    # FIXME: fails on most decorators, currying, and such...
    #        (could look for magic __wrapped__ or __func__ attr)
    #        (could fix in 'namespace' to check obj for closure)
    if verify and not head.startswith("mbodi."):  # weird behavior for dill
        try:
            exec(_str)  # XXX: check if == obj? (name collision)
        except ImportError:  # XXX: better top-down or bottom-up recursion?
            _head = head.rsplit(".", 1)[0]  # (or get all, then compare == obj?)
            if not _head:
                raise
            if _head != head:
                _str = _getimport(_head, tail, alias, verify)
    return _str


def getname(obj, force=False, fqn=False):  # XXX: throw(?) to raise error on fail?
    """Get the name of the obj. For lambdas, get the name of the pointer."""
    if fqn:
        return ".".join(_namespace(obj))
    module = getmodule(obj)
    if not module:  # things like "None" and "1"
        if not force:
            return None
        return repr(obj)
    try:
        # XXX: 'wrong' for decorators and curried functions ?
        #       if obj.func_closure: ...use logic from getimportable, etc ?
        name = obj.__name__
        if name == "<lambda>":
            return getsource(obj).split("=", 1)[0].strip()
        # handle some special cases
        if module.__name__ in ["builtins", "__builtin__"] and name == "ellipsis":
            name = "EllipsisType"
        return name
    except AttributeError:  # XXX: better to just throw AttributeError ?
        if not force:
            return None
        name = repr(obj)
        if name.startswith("<"):  # or name.split('('):
            return None
        return name


def _outdent(lines, spaces=None, all=True):
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


def outdent(code, spaces=None, all=True):
    """Outdent a block of code (default is to strip all leading whitespace)."""
    indent = indentsize(code)
    if spaces is None or spaces > indent or spaces < 0:
        spaces = indent
    # XXX: will this delete '\n' in some cases?
    if not all:
        return code[spaces:]
    return "\n".join(_outdent(code.split("\n"), spaces=spaces, all=all))


def _enclose(obj, alias=""):  # FIXME: needs alias to hold returned obj
    """Create a function enclosure around the source of some obj."""
    dummy = "__this_is_a_big_dummy_enclosing_function__"

    stub = "__this_is_a_stub_variable__"
    code = f"def {dummy}():\n"
    code += indent(getsource(obj, alias=stub, lstrip=True, force=True))
    code += indent(f"return {stub}\n")
    if alias:
        code += f"{alias} = "
    code += f"{dummy}(); del {dummy}\n"
    return code

def dumpsource(obj, alias="", new=False, enclose=True):
    """'dump to source', where the code includes a pickled obj.

    If new=True and obj is a class instance, then create a new
    instance using the unpacked class source code. If enclose, then
    create the obj inside a function enclosure (thus minimizing
    any global namespace pollution).
    """
    mlink = importmodule("mlink", safe=True)
    pik = repr(mlink.dumps(obj))
    code = "import mlink\n"
    if enclose:
        stub = "__this_is_a_stub_variable__" 
        pre = f"{stub} = "
        new = False  # FIXME: new=True doesn't work with enclose=True
    else:
        stub = alias
        pre = f"{stub} = " if alias else alias

    # if a 'new' instance is not needed, then just dump and load
    if not new or not _isinstance(obj):
        code += pre + f"mlink.loads({pik})\n"
    else:  # XXX: other cases where source code is needed???
        code += getsource(obj.__class__, alias="", lstrip=True, force=True)
        mod = repr(obj.__module__)  # should have a module (no builtins here)
        code += pre + f'mlink.loads({pik}.replace(b{mod},bytes(__name__,"UTF-8")))\n'

    if enclose:
        # generation of the 'enclosure'
        dummy = "__this_is_a_big_dummy_obj__"
        dummy = _enclose(dummy, alias=alias)
        # hack to replace the 'dummy' with the 'real' code
        dummy = dummy.split("\n")
        code = dummy[0] + "\n" + indent(code) + "\n".join(dummy[-3:])

    return code  # XXX: better 'dumpsourcelines', returning list of lines?


def getsource(obj, alias="", lstrip=False, enclosing=False, force=False, builtin=False):
    """Return the text of the source code for an obj.

    The source code for
    interactively-defined objs are extracted from the interpreter's history.

    The argument may be a module, class, method, function, traceback, frame,
    or code obj.  The source code is returned as a single string.  An
    IOError is raised if the source code cannot be retrieved, while a
    TypeError is raised for objs where the source code is unavailable
    (e.g. builtins).

    If alias is provided, then add a line of code that renames the obj.
    If lstrip=True, ensure there is no indentation in the first line of code.
    If enclosing=True, then also return any enclosing code.
    If force=True, catch (TypeError,IOError) and try to use import hooks.
    If builtin=True, force an import for any builtins
    """
    # hascode denotes a callable
    hascode = _hascode(obj)
    # is a class instance type (and not in builtins)
    instance = _isinstance(obj)

    # get source lines; if fail, try to 'force' an import
    try:  # fails for builtins, and other assorted obj types
        lines, lnum = getsourcelines(obj, enclosing=enclosing)
    except (TypeError, IOError):  # failed to get source, resort to import hooks
        if not force:  # don't try to get types that findsource can't get
            raise
        if not getmodule(obj):  # get things like 'None' and '1'
            if not instance:
                return getimport(obj, alias, builtin=builtin)
            # special handling (numpy arrays, ...)
            _import = getimport(obj, builtin=builtin)
            name = getname(obj, force=True)
            _alias = f"{alias} = " if alias else ""
            if alias == name:
                _alias = ""
            return _import + _alias + "%s\n" % name

        if not instance:
            return getimport(obj, alias, builtin=builtin)
        # now we are dealing with an instance...
        name = obj.__class__.__name__
        module = obj.__module__
        if module in ["builtins", "__builtin__"]:
            return getimport(obj, alias, builtin=builtin)

        lines, lnum = [f"{name} = __import__('{module}', fromlist=['{name}']).{name}\n"], 0
        obj = eval(lines[0].lstrip(name + " = "))  # noqa: S307
        lines, lnum = getsourcelines(obj, enclosing=enclosing)

    # strip leading indent (helps ensure can be imported)
    if lstrip or alias:
        lines = _outdent(lines)

    # instantiate, if there's a nice repr  #XXX: BAD IDEA???
    if instance:  # and force: #XXX: move into findsource or getsourcelines ?
        if "(" in repr(obj):
            lines.append("%r\n" % obj)
        # else: #XXX: better to somehow to leverage __reduce__ ?
        #    reconstructor,args = obj.__reduce__()
        #    _ = reconstructor(*args)
        else:  # fall back to serialization #XXX: bad idea?
            # XXX: better not duplicate work? #XXX: better new/enclose=True?
            lines = dumpsource(obj, alias="", new=force, enclose=False)
            lines, lnum = [line + "\n" for line in lines.split("\n")][:-1], 0

    # add an alias to the source code
    if alias:
        if hascode:
            skip = 0
            for line in lines:  # skip lines that are decorators
                if not line.startswith("@"):
                    break
                skip += 1
            # XXX: use regex from findsource / getsourcelines ?
            if lines[skip].lstrip().startswith("def "):  # we have a function
                if alias != obj.__name__:
                    lines.append(f"\n{alias} = {obj.__name__}\n")
            elif "lambda " in lines[skip]:  # we have a lambda
                if alias != lines[skip].split("=")[0].strip():
                    lines[skip] = f"{alias} = {lines[skip]}"
            else:  # ...try to use the obj's name
                if alias != obj.__name__:
                    lines.append(f"\n{alias} = {obj.__name__}\n")
        else:  # class or class instance
            if instance:
                if alias != lines[-1].split("=")[0].strip():
                    lines[-1] = (f"{alias} = ") + lines[-1]
            else:
                name = getname(obj, force=True) or obj.__name__
                if alias != name:
                    lines.append(f"\n{alias} = {name}\n")
    return "".join(lines)


def getblocks(obj,*, lstrip=False, enclosing=False, locate=False):
    """Return a list of source lines and starting line number for an obj.

    Interactively-defined objs refer to lines in the interpreter's history.

    If enclosing=True, then also return any enclosing code.
    If lstrip=True, ensure there is no indentation in the first line of code.
    If locate=True, then also return the line number for the block of code.

    DEPRECATED: use 'getsourcelines' instead
    """
    lines, lnum = findsource(obj)

    if ismodule(obj):
        if lstrip:
            lines = _outdent(lines)
        return ([lines], [0]) if locate is True else [lines]

    # XXX: 'enclosing' means: closures only? or classes and files?
    indent = indentsize(lines[lnum])
    block = getblock(lines[lnum:])  # XXX: catch any TokenError here?

    if not enclosing or not indent:
        if lstrip:
            block = _outdent(block)
        return ([block], [lnum]) if locate is True else [block]

    pat1 = r"^(\s*def\s)|(.*(?<!\w)lambda(:|\s))"
    pat1 = re.compile(pat1)
    pat2 = r"^(\s*@)"
    pat2 = re.compile(pat2)
    # pat3 = r'^(\s*class\s)'; pat3 = re.compile(pat3) #XXX: enclosing class?
    # FIXME: bound methods need enclosing class (and then instantiation)
    #       *or* somehow apply a partial using the instance

    skip = 0
    line = 0
    blocks = []
    _lnum = []
    target = "".join(block)
    while line <= lnum:  # XXX: repeat lnum? or until line < lnum?
        # see if starts with ('def','lambda') and contains our target block
        if pat1.match(lines[line]):
            if not skip:
                try:
                    code = getblock(lines[line:])
                except TokenError:
                    code = [lines[line]]
            if indentsize(lines[line]) > indent:  # XXX: should be >= ?
                line += len(code) - skip
            elif target in "".join(code):
                blocks.append(code)  # save code block as the potential winner
                _lnum.append(line - skip)  # save the line number for the match
                line += len(code) - skip
            else:
                line += 1
            skip = 0
        # find skip: the number of consecutive decorators
        elif pat2.match(lines[line]):
            try:
                code = getblock(lines[line:])
            except Exception:
                code = [lines[line]]
            skip = 1
            for _line in code[1:]:  # skip lines that are decorators
                if not pat2.match(_line):
                    break
                skip += 1
            line += skip
        # no match: reset skip and go to the next line
        else:
            line += 1
            skip = 0

    if not blocks:
        blocks = [block]
        _lnum = [lnum]
    if lstrip:
        blocks = [_outdent(block) for block in blocks]
    # return last match
    return (blocks, _lnum) if locate is True else blocks


def hascode(obj):
    """True if obj has an attribute that stores it's __code__."""
    return getattr(obj, "__code__", None) or getattr(obj, "func_code", None)


def isanyinstance(obj):
    """True if obj is a class instance type (and is not a builtin)."""
    if hascode(obj) or isclass(obj) or ismodule(obj):
        return False
    if istraceback(obj) or isframe(obj) or iscode(obj):
        return False
    # special handling (numpy arrays, ...)
    if not getmodule(obj) and getmodule(type(obj)).__name__ in ["numpy"]:
        return True
    _types = ("<class ", "<type 'instance'>")
    if not repr(type(obj)).startswith(_types):  # FIXME: weak hack
        return False
    return not (getmodule(obj) and obj.__module__ not in ["builtins", "__builtin__"] and getname(obj, force=True) not in ["array"])



def isintypes(obj):
    """Check if obj is in the 'types' module."""
    import types

    # allow user to pass in obj or obj.__name__
    if type(obj) is not str:
        obj = getname(obj, force=True)
    if obj == "ellipsis":
        obj = "EllipsisType"
    return hasattr(types, obj)


def indent(code, spaces=4):
    """Indent a block of code with whitespace (default is 4 spaces)."""
    indent = indentsize(code)
    if type(spaces) is int:
        spaces = " " * spaces
    # if '\t' is provided, will indent with a tab
    nspaces = indentsize(spaces)
    # blank lines (etc) need to be ignored
    lines = code.split("\n")
    ##  stq = "'''"; dtq = '"""'
    ##  in_stq = in_dtq = False
    for i in range(len(lines)):
        # FIXME: works... but shouldn't indent 2nd+ lines of multiline doc
        _indent = indentsize(lines[i])
        if indent > _indent:
            continue
        lines[i] = spaces + lines[i]
    if lines[-1].strip() == "":
        lines[-1] = ""
    return "\n".join(lines)


def getmodule(obj, filename=None, force=False):
    """Get the module of the obj."""
    from inspect import getmodule as getmod

    module = getmod(obj, filename)
    if module or not force:
        return module
    import builtins

    from minspect.source import getname

    name = getname(obj, force=True)
    return builtins if name in vars(builtins) else None


def getsourcelines(obj, lstrip=False, enclosing=False):
    """Return a list of source lines and starting line number for an obj.

    Interactively-defined objs refer to lines in the interpreter's history.

    The argument may be a module, class, method, function, traceback, frame,
    or code obj.  The source code is returned as a list of the lines
    corresponding to the obj and the line number indicates where in the
    original source file the first line of code was found.  An IOError is
    raised if the source code cannot be retrieved, while a TypeError is
    raised for objs where the source code is unavailable (e.g. builtins).

    If lstrip=True, ensure there is no indentation in the first line of code.
    If enclosing=True, then also return any enclosing code.
    """
    code, n = getblocks(obj, lstrip=lstrip, enclosing=enclosing, locate=True)
    return code[-1], n[-1]


def outermost(func):
    """Get outermost enclosing obj (i.e. the outer function in a closure).

    NOTE: this is the obj-equivalent of getsource(func, enclosing=True)
    """
    if ismethod(func):
        _globals = func.__func__.__globals__ or {}
    elif isfunction(func):
        _globals = func.__globals__ or {}
    _globals = _globals.items()
    # get the enclosing source

    try:
        lines, lnum = getsourcelines(func, enclosing=True)
    except Exception:  # TypeError, IOError
        lines, lnum = [], None
    code = "".join(lines)
    # get all possible names,objs that are named in the enclosing source
    _locals = ((name, obj) for (name, obj) in _globals if name in code)
    # now only save the objs that generate the enclosing block
    for name, obj in _locals:  # XXX: don't really need 'name'
        try:
            if getsourcelines(obj) == (lines, lnum):
                return obj
        except( TypeError, IOError):
            pass
    return None


def nestedcode(func, recurse=True):  # XXX: or return dict of {co_name: co} ?
    """Get the code objs for any nested functions (e.g. in a closure)."""
    func = code(func)
    if not iscode(func):
        return []  # XXX: or raise? no matches
    nested = set()
    for co in func.co_consts:
        if co is None:
            continue
        co = code(co)
        if co:
            nested.add(co)
            if recurse:
                nested |= set(nestedcode(co, recurse=True))
    return list(nested)


def code(func):
    """Get the code obj for the given function or method.

    NOTE: use minspect.source.getsource(CODEOBJ) to get the source code
    """
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
    return


# XXX: ugly: parse dis.dis for name after "<code obj" in line and in globals?
def referrednested(func, recurse=True):  # XXX: return dict of {__name__: obj} ?
    """Get functions defined inside of func (e.g. inner functions in a closure).

    NOTE: results may differ if the function has been executed or not.
    If len(nestedcode(func)) > len(referrednested(func)), try calling func().
    If possible, python builds code objs, but delays building functions
    until func() is called.
    """
    import gc

    funcs = set()
    # get the code objs, and try to track down by referrence
    for co in nestedcode(func, recurse):
        # look for function objs that refer to the code obj
        for obj in gc.get_referrers(co):
            # get methods
            _ = getattr(obj, "__func__", None)  # ismethod
            if getattr(_, "__code__", None) is co or\
                getattr(obj, "__code__", None) is co or\
                getattr(obj, "f_code", None) is co or\
                hasattr(obj, "co_code") and obj is co:
                funcs.add(obj)
    #     frameobjs => func.__code__.co_varnames not in func.__code__.co_cellvars
    #     funcobjs => func.__code__.co_cellvars not in func.__code__.co_varnames
    #     frameobjs are not found, however funcobjs are...
    #     (see: test_mixins.quad ... and test_mixins.wtf)
    #     after execution, code objs get compiled, and then may be found by gc
    return list(funcs)


def freevars(func):
    """Get objs defined in enclosing code that are referred to by func.

    returns a dict of {name:obj}
    """
    if ismethod(func):
        func = func.__func__
    if isfunction(func):
        closures = func.__closure__ or ()
        func = func.__code__.co_freevars  # get freevars
    else:
        return {}

    def get_cell_contents():
        for name, c in zip(func, closures):
            try:
                cell_contents = c.cell_contents
            except ValueError:  # cell is empty
                continue
            yield name, c.cell_contents

    return dict(get_cell_contents())


def nestedglobals(func, recurse=True) -> list:
    """Get the names of any globals found within func."""
    func = code(func)
    if func is None:
        return []
    import sys

    from minspect._internal import capture

    can_null = sys.hexversion >= 0x30B00A7  # NULL may be prepended >= 3.11a7
    names = set()
    with capture("stdout") as out:
        dis.dis(func) 
    for line in out.getvalue().splitlines():
        if "_GLOBAL" in line:
            name = line.split("(")[-1].split(")")[0]
            if can_null:
                names.add(name.replace("NULL + ", "").replace(" + NULL", ""))
            else:
                names.add(name)
    for co in getattr(func, "co_consts", ()):
        if co and recurse and iscode(co):
            names.update(nestedglobals(co, recurse=True))
    return list(names)
