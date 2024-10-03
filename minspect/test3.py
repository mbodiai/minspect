import importlib
import inspect
import sys
import unittest
from pathlib import Path
from typing import LiteralString


def generate_html_like_markdown(module_name, max_depth=5) -> str | LiteralString:
    """Generates an HTML-like markdown structure with collapsible sections for any Python module dynamically using introspection.

    Includes method and function signatures, docstrings, attributes, organized with clear formatting and hierarchy.
    """
    try:
        module = importlib.import_module(module_name)
    except ImportError as e:
        return f"Error importing module: {str(e)}"

    markdown_output = []

    def process_item(item, depth=1, name=None):
        if depth > max_depth:
            return

        indent = "  " * (depth - 1)
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

    def process_module(item, depth, indent, tag):
        markdown_output.append(f"{indent}<details><summary><{tag}>module {item.__name__}</{tag}></summary>\n")
        sub_items = dir(item)
        for sub_name in sub_items:
            if not sub_name.startswith("_"):
                sub_item = getattr(item, sub_name)
                process_item(sub_item, depth + 1, sub_name)
        markdown_output.append(f"{indent}</details>\n")

    def process_class(item, depth, indent, tag):
        class_signature = f"class {item.__name__}({', '.join(base.__name__ for base in item.__bases__)})"
        markdown_output.append(f"{indent}<details><summary><{tag}>{class_signature}</{tag}></summary>\n")
        for sub_name, value in inspect.getmembers(item):
            if inspect.isfunction(value) or inspect.ismethod(value):
                process_function(value, sub_name, indent, tag)
            elif not sub_name.startswith("_"):
                markdown_output.append(f"{indent}<li><b>{sub_name}:</b> {repr(value)}</li>\n")
        markdown_output.append(f"{indent}</details>\n")

    def process_function(item, name, indent, tag):
        function_signature = f"def {item.__name__}{inspect.signature(item)}"
        markdown_output.append(f"{indent}<details><summary><b>{function_signature}</b></summary>\n")
        function_doc = inspect.getdoc(item)
        if function_doc:
            markdown_output.append(f"{indent}<p>{function_doc}</p>\n")
        markdown_output.append(f"{indent}</details>\n")

    process_item(module)
    return "".join(markdown_output)


class TestHTMLLikeMarkdown(unittest.TestCase):
    def test_html_like_markdown(self):
        module_name = "math"  # Using math module as an example for simplicity
        expected_output_part = "<details><summary><h3>module math</h3></summary>"
        output = generate_html_like_markdown(module_name, max_depth=2)
        self.assertIn(expected_output_part, output, "The expected HTML structure is not found in the output.")


# Running the unittest
if __name__ == "__main__":
    output = generate_html_like_markdown("pydantic", max_depth=2)
    from rich.console import Console
    from rich.markdown import Markdown
    Path(sys.argv[1] if len(sys.argv) > 1 else "output.md").write_text(output)
    console = Console()
    console.print(Markdown(output))
