import inspect
import importlib
from pathlib import Path

def generate_collapsible_markdown_no_source(module_name, max_depth=5):
    """
    Generates a markdown structure with collapsible sections for any Python module dynamically using introspection.
    Excludes the source code, focusing on signatures, attributes, and hierarchy.
    """
    module = importlib.import_module(module_name)
    markdown_output = []

    def process_item(item, depth=1, name=None):
        if depth > max_depth:
            return

        indent = '  ' * (depth - 1)

        if inspect.ismodule(item):
            # For modules, just use the name in backticks
            markdown_output.append(f"{indent}<details><summary>`{item.__name__}`</summary>\n")
            sub_items = dir(item)
            for sub_name in sub_items:
                if sub_name.startswith('_'):
                    continue
                sub_item = getattr(item, sub_name)
                process_item(sub_item, depth + 1, sub_name)
            markdown_output.append(f"{indent}</details>\n")
        elif inspect.isclass(item):
            # For classes, display their signature with backticks
            class_signature = f"class {item.__name__}({', '.join(base.__name__ for base in item.__bases__)})"
            markdown_output.append(f"{indent}<details><summary>`{class_signature}`</summary>\n")
            # Iterate over class members
            for sub_name, value in inspect.getmembers(item):
                if inspect.isfunction(value) or inspect.ismethod(value):
                    try:
                        sig = inspect.signature(value)
                        markdown_output.append(f"{indent}  <details><summary>`{sub_name} {sig}`</summary>\n")
                        markdown_output.append(f"{indent}  </details>\n")
                    except ValueError:
                        markdown_output.append(f"{indent}  - `{sub_name} <signature unavailable>`\n")
                elif not sub_name.startswith('_'):
                    markdown_output.append(f"{indent}  - `{sub_name} = {repr(value)}`\n")
            markdown_output.append(f"{indent}</details>\n")
        elif inspect.isfunction(item) or inspect.ismethod(item):
            # For functions, display their signature with backticks (no source code)
            try:
                sig = inspect.signature(item)
                markdown_output.append(f"{indent}<details><summary>`{name} {sig}`</summary>\n")
                markdown_output.append(f"{indent}</details>\n")
            except ValueError:
                markdown_output.append(f"{indent}- `{name} <signature unavailable>`\n")
        elif name:
            # For attributes and other items at module or class level
            markdown_output.append(f"{indent}- `{name} = {repr(item)}`\n")

    process_item(module)
    return "".join(markdown_output)

# Now, save the generated markdown to a file and provide a download link

def save_markdown_to_file(module_name, file_path, max_depth=5):
    """Generates a markdown structure with collapsible sections and saves it to a file."""
    markdown_output = generate_collapsible_markdown_no_source(module_name, max_depth)
    
    # Save to the specified file
    with Path(file_path).open('w') as file:
        file.write(markdown_output)
        
    return file_path

# Example: Generate the markdown for pydantic module up to depth 5 and save it to a file
file_path = 'pydantic_markdown_depth_5.md'
save_markdown_to_file('pydantic', file_path, max_depth=5)

# The generated markdown can be downloaded from the specified file path