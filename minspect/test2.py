import importlib
import inspect
from typing import LiteralString


def generate_html_like_markdown(module_name, max_depth=5) -> LiteralString:
    """Generates an HTML-like markdown structure with collapsible sections for any Python module dynamically using introspection.

    Includes method and function signatures, docstrings, attributes, organized with clear formatting and hierarchy.
    """
    module = importlib.import_module(module_name)
    markdown_output = []

    def process_item(item, depth=1, name=None):
        if depth > max_depth:
            return

        indent = "  " * (depth - 1)
        tag = "h" + str(min(depth + 2, 6))  # Use heading tags from h2 to h5

        if inspect.ismodule(item):
            markdown_output.append(f"{indent}<details><summary><{tag}>module {item.__name__}</{tag}></summary>\n")
            sub_items = dir(item)
            for sub_name in sub_items:
                if sub_name.startswith("_"):
                    continue
                sub_item = getattr(item, sub_name)
                process_item(sub_item, depth + 1, sub_name)
            markdown_output.append(f"{indent}</details>\n")
        elif inspect.isclass(item):
            class_signature = f"class {item.__name__}({', '.join(base.__name__ for base in item.__bases__)})"
            markdown_output.append(f"{indent}<details><summary><{tag}>{class_signature}</{tag}></summary>\n")
            class_doc = inspect.getdoc(item)
            if class_doc:
                markdown_output.append(f"{indent}<li>{class_doc.split('.')[0]}.</li>\n")
            for sub_name, value in inspect.getmembers(item):
                if inspect.isfunction(value) or inspect.ismethod(value):
                    function_signature = f"def {value.__name__}{inspect.signature(value)}"
                    markdown_output.append(f"{indent}<details><summary><b>{function_signature}</b></summary>\n")
                    function_doc = inspect.getdoc(value)
                    if function_doc:
                        markdown_output.append(f"{indent}<p>{function_doc}</p>\n")
                    markdown_output.append(f"{indent}</details>\n")
                elif not sub_name.startswith("_"):
                    markdown_output.append(f"{indent}<li><b>{sub_name}:</b> {repr(value)}</li>\n")
            markdown_output.append(f"{indent}</details>\n")
        elif inspect.isfunction(item) or inspect.ismethod(item):
            function_signature = f"def {item.__name__}{inspect.signature(item)}"
            markdown_output.append(f"{indent}<details><summary><b>{function_signature}</b></summary>\n")
            function_doc = inspect.getdoc(item)
            if function_doc:
                markdown_output.append(f"{indent}<p>{function_doc}</p>\n")
            markdown_output.append(f"{indent}</details>\n")
        elif name:
            markdown_output.append(f"{indent}<li><b>{name}:</b> {repr(item)}</li>\n")

    process_item(module)
    return "".join(markdown_output)


# Generate the HTML-like markdown for pydantic up to depth 5
pydantic_html_markdown = generate_html_like_markdown("pydantic", max_depth=5)

# Example output (not fully rendered here due to length)
print(pydantic_html_markdown[:1000])  # Print the first 1000 characters to check the structure
