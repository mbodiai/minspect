import importlib
from importlib.machinery import ModuleSpec
import inspect
import os
from pathlib import Path
import pydoc
import traceback

import rich_click as click
from rich.console import Console
console = Console()

def generate_html_like_markdown(module_name: str, max_depth: int = 2, docs: bool = False) -> str:
    """Generates an HTML-like markdown structure with collapsible sections for any Python module dynamically using introspection.

    Includes method and function signatures, docstrings, attributes, organized with clear formatting and hierarchy.
    
    TODO: Add pyclbr, pydoc summary, pydoc path discover, and make everything a link. colorize as well
    """
    try:
        module = importlib.import_module(module_name)
    except ImportError as e:
        return f"Error importing module: {str(e)}"
    
    markdown_output = []

    def process_item(item, depth=1, name=None):
        if depth > max_depth:
            return

        indent = '  ' * (depth - 1)
        tag = "h" + str(min(depth + 2, 6))  # Use heading tags from h3 to h6

        try:
            if inspect.ismodule(item):
                process_module(item, depth, indent, tag)
            elif inspect.isclass(item):
                process_class(item, depth, indent, tag)
            elif inspect.isfunction(item) or inspect.ismethod(item):
                process_function(item, name, indent, tag)
            elif name:
                markdown_output.append(f"{indent}<li><b>{name}:</b> {repr(item)}</li>\n")
        except Exception as e:
            markdown_output.append(f"{indent}<!-- Error processing item: {str(e)} -->\n")
            traceback.print_exc()

    def process_module(item, depth, indent, tag):
        markdown_output.append(f"{indent}<details><summary><{tag}>module {item.__name__}</{tag}></summary>\n")
        sub_items = dir(item)
        for sub_name in sub_items:
            if not sub_name.startswith('_'):
                sub_item = getattr(item, sub_name)
                process_item(sub_item, depth + 1, sub_name)
        markdown_output.append(f"{indent}</details>\n")

    def process_class(item, depth, indent, tag):
        class_signature = f"class {item.__name__}({', '.join(base.__name__ for base in item.__bases__)})"
        markdown_output.append(f"{indent}<details><summary><{tag}>{class_signature}</{tag}></summary>\n")
        for sub_name, value in inspect.getmembers(item):
            if inspect.isfunction(value) or inspect.ismethod(value):
                process_function(value, sub_name, indent, tag)
            elif not sub_name.startswith('_'):
                markdown_output.append(f"{indent}<li><b>{sub_name}:</b> {repr(value)}</li>\n")
        markdown_output.append(f"{indent}</details>\n")

    def process_function(item, name, indent, tag):
        function_signature = f"def {item.__name__}{inspect.signature(item)}"
        markdown_output.append(f"{indent}<details><summary><b>{function_signature}</b></summary>\n")
        function_doc = inspect.getdoc(item)
        if function_doc and docs:
            markdown_output.append(f"{indent}<p>{function_doc}</p>\n")
        markdown_output.append(f"{indent}</details>\n")

    process_item(module)
    return "".join(markdown_output)


@click.command()
@click.argument("modules",type=str, nargs=-1)
@click.option("--dirs", "-d", multiple=True, help="Directories to inspect")
@click.option("--max-depth", "-D", default=2, help="Maximum depth to inspect")
@click.option("--exclude", "-e", multiple=True, help="Modules to exclude")
@click.option("--output-file", "-o", default="output.md", help="Output file")
@click.option("--docs", "-D", is_flag=True, help="Include docstrings")
@click.option("--ai-prompt", is_flag=True, help="Query AI to answer questions")
def main(modules: list[str], dirs: list[str | Path], max_depth: int, exclude: list[str], output_file: str, docs: bool, ai=False):
    """Generate a markdown file from Python modules."""
    from importlib.util import find_spec
    if not modules and not dirs:
        dirs = [Path.cwd()]
    elif modules:
        dirs =[]
        for m in modules:
            spec = getattr(find_spec(m), "origin", ".")
            if not spec:
                console.print(f"Module {m} not found")
                continue
            dirs.append(Path(spec).parent)
    output_file = str(Path(output_file).resolve())
    if output_file:
        with Path(output_file).open("w") as f:
            f.write("")
    for d in set(dirs) - set(exclude):
        os.chdir(d)
        
            
        for m in modules:
            for line in generate_html_like_markdown(m,max_depth,docs).splitlines():
                console.print(line)
                
                if output_file:
                    with Path(output_file).open("a") as f:
                        f.write(line + "\n")


if __name__ == "__main__":
    from pprint import pprint
    main()
