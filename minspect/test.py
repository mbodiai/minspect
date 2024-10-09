import ast
import gc
import importlib
import inspect
import sys
import time
import traceback
from pathlib import Path
from pyclbr import readmodule, readmodule_ex
from pydoc import getdoc, getpager, locate, pathdirs, splitdoc
from typing import List, Optional

visit: set = set()
def get_first_sentence(docstring: str) -> str:
    """Extracts the first sentence from a docstring."""
    if not docstring:
        return ""
    return splitdoc(docstring)[0]

def format_signature(obj) -> str:
    """Formats the signature of a class or function."""
    if inspect.isclass(obj):
        return f"class {obj.__name__}:"
    elif inspect.isfunction(obj) or inspect.ismethod(obj):
        sig = inspect.signature(obj)
        return f"def {obj.__name__}{sig}:"
    return ""

class DetailsManager:
    """A context manager to handle <details> tags with proper indentation."""
    def __init__(self, markdown: List[str], summary: str, indent: int = 0):
        self.markdown = markdown
        self.summary = summary
        self.indent = indent

    def __enter__(self):
        indent_space = '  ' * self.indent
        self.markdown.append(f'{indent_space}')
        self.markdown.append(f'{indent_space}  <summary>{self.summary}</summary>')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        indent_space = '  ' * self.indent
        self.markdown.append(f'{indent_space}</details>\n')

def parse_input(input_str: str) -> List[str]:
    """Parses the input string and returns a list of access paths.

    Supports 'module:class.attr' and 'module.class.attr' syntax.
    """
    if ':' in input_str:
        module_part, attr_part = input_str.split(':', 1)
    else:
        parts = input_str.split('.')
        module_part = parts[0]
        attr_part = '.'.join(parts[1:])

    return [module_part] + attr_part.split('.')

def find_object(module, access_path: List[str]):
    """Traverses the module based on the access path and returns the target object."""
    current = module
    for part in access_path[1:]:
        if hasattr(current, part):
            current = getattr(current, part)
        else:
            return None
    return current

def generate_markdown(module_name: str, access_path: Optional[str] = None) -> str:
    """Generates collapsed nested Markdown documentation for a Python module or specific attribute."""
    try:
        module = importlib.import_module(module_name)
    except ImportError:
        return f"**Error:** Module '{module_name}' could not be imported."

    module_doc = inspect.getdoc(module)
    first_sentence = get_first_sentence(module_doc) if module_doc else ""

    markdown = []
    
    if access_path:
        access_parts = parse_input(access_path)
        if access_parts[0] != module_name:
            return f"**Error:** The specified module '{access_parts[0]}' does not match the target module '{module_name}'."
        target_obj = find_object(module, access_parts)
        if not target_obj:
            return f"**Error:** The specified path '{access_path}' was not found in the module '{module_name}'."
        # Generate documentation for the specific object
        with DetailsManager(markdown, f'<h3>{".".join(access_parts)}.</h3>'):
            process_object(target_obj, markdown, indent=1)
    else:
        # Module-level Documentation
        with DetailsManager(markdown, f'<h3>{module_name}</h3>'):
            with DetailsManager(markdown, first_sentence, indent=1):
                markdown.append(f'    {module_doc or "No module docstring provided."}\n')

            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) or inspect.isfunction(obj):
                    markdown.extend(process_object(obj, [], indent=1))

    return "\n".join(markdown)

def process_object(obj, markdown: List[str], indent: int) -> List[str]:
    """Processes an object (class or function) and appends its Markdown representation."""
    if inspect.isclass(obj):
        return process_class(obj, indent)
    if inspect.isfunction(obj):
        return process_function(obj, indent)
    markdown.append("    - **Unsupported type:** Only classes and functions are supported.\n")
    return markdown

def process_class(cls, indent: int) -> List[str]:
    """Processes a class object and returns its Markdown representation."""
    if cls in visit:
        return []
    visit.add(cls)
    class_doc = inspect.getdoc(cls)

    markdown = []
    with DetailsManager(markdown, f'<b>{cls.__name__}</b>', indent=indent):
        # Class Signature and Documentation
        with DetailsManager(markdown, f'class {cls.__name__}:', indent=indent + 1):
            markdown.append(f' - **Documentation**: {class_doc or "No documentation provided."}')
        
        # Methods and Nested Classes
        for name, member in inspect.getmembers(cls):
            if inspect.isfunction(member) or inspect.ismethod(member):
                markdown.extend(process_function(member, indent=indent + 1))
            elif inspect.isclass(member):
                markdown.extend(process_class(member, indent=indent + 1))
    return markdown

def process_function(func, indent: int) -> List[str]:
    """Processes a function or method object and returns its Markdown representation."""
    func_doc = inspect.getdoc(func)
    signature = format_signature(func)
    markdown = []
    with DetailsManager(markdown, f'<b>{func.__name__}</b>', indent=indent):
        markdown.append(f' - **Signature**: `{signature}`')
        markdown.append(f' - **Documentation**: {func_doc or "No documentation provided."}\n')
        
        # Source Code
        source = get_source_code(func)
        if source:
            with DetailsManager(markdown, "Source Code", indent=indent + 1):
                source_indented = '\n'.join(['    ' + line for line in source.split('\n')])
                markdown.append(f'    ```python\n{source_indented}\n    ```')
    return markdown

def get_source_code(obj) -> Optional[str]:
    """Retrieves the source code for a given object."""
    try:
        source = inspect.getsource(obj)
        return source
    except Exception:
        return None

def maybe_expand_dir(path: str) -> Path:
    """Expands the user directory in a given path."""
    try:
        return Path(path).expanduser().resolve()
    except FileNotFoundError:
        try:
            return Path(path).resolve()
        except FileNotFoundError:
            try:
                return Path(path)
            except FileNotFoundError:
                return None

def bfs_dir(dir: Path):
    """Breadth-first search of a directory."""
    queue = [dir]
    while queue:
        current = queue.pop(0)
        yield current
        if current.is_dir():
            queue.extend(current.iterdir())
    return
        

    
if __name__ == "__main__":
    import argparse
    from importlib import reload

    from mbpy.commands import run_cmd

    from minspect.source import importmodule
    parser = argparse.ArgumentParser(description="Generate collapsed nested Markdown documentation for a Specific class or callable in the format 'module:Class.method' or 'module.Class.method'")
    parser.add_argument("path_module_or_package", help="Format 'path'/package.module:Class.method or package.module:Class.method")

    args = parser.parse_args()
    obj = args.path_module_or_package
    obj = bfs_dir(dir) if (dir := maybe_expand_dir(obj)) else [obj] # noqa: A001
    

    
    try:
        module = importmodule(args.module_name)
    except ImportError:
      
        try:
          run_cmd(f"{sys.executable} -m pip install {args.module_name}")
          time.sleep(10)
          module = reload(importlib.import_module(args.module_name))

        except Exception as e:
          print(f"Error: Module '{args.module_name}' could not be imported. {str(e)}")
          traceback.print_exc()
          sys.exit(1)

    markdown_output = generate_markdown(args.module_name, args.access)
    print(markdown_output)
    Path("output.md").write_text(markdown_output)

