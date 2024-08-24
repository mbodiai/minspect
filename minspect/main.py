import sys
from click import argument, command, option, help_option

from minspect.inspecting import inspect_library


@command()
@help_option('-h', '--help')
@argument("module_or_class", type=str)
@option("--depth", "-d", type=int, default=0, help="Depth to inspect")
@option("--sigs", "-s", is_flag=True, help="Include function signatures")
@option("--docs", "-doc", is_flag=True, help="Include docstrings")
@option("--code", "-c", is_flag=True, help="Include source code")
@option("--imports", "-imp", is_flag=True, help="Include imports")
@option("--all", "-a", is_flag=True, help="Include all")
@option("--markdown", "-md", is_flag=True, help="Output as markdown")
def cli(module_or_class, depth, sigs, docs, code, imports, all, markdown):
    """Inspect a Python module or class. Optionally create a markdown file."""
    try:
        result = inspect_library(module_or_class, depth, sigs, docs, code, imports, all, markdown)
    
        if markdown:
            print("# Inspection Result")
            for name, info in result.items():
                print(f"\n## {name}")
                if 'type' in info:
                    print(f"**Type:** {info['type']}")
                if 'path' in info:
                    print(f"**Path:** {info['path']}")
                if 'signature' in info:
                    print(f"\n**Signature:**\n```python\n{info['signature']}\n```")
                if 'docstring' in info:
                    print(f"\n**Docstring:**\n```\n{info['docstring']}\n```")
                if 'code' in info:
                    print(f"\n**Source Code:**\n```python\n{info['code']}\n```")
                if 'members' in info:
                    print("\n### Members")
                    for member_name, member_info in info['members'].items():
                        print(f"\n#### {member_name}")
                        if 'type' in member_info:
                            print(f"**Type:** {member_info['type']}")
                        if 'path' in member_info:
                            print(f"**Path:** {member_info['path']}")
                        if 'signature' in member_info:
                            print(f"\n**Signature:**\n```python\n{member_info['signature']}\n```")
                        if 'docstring' in member_info:
                            print(f"\n**Docstring:**\n```\n{member_info['docstring']}\n```")
                        if 'code' in member_info:
                            print(f"\n**Source Code:**\n```python\n{member_info['code']}\n```")
        else:
            for name, info in result.items():
                print(f"{name}:")
                if 'type' in info:
                    print(f"  Type: {info['type']}")
                if 'path' in info:
                    print(f"  Path: {info['path']}")
                if 'signature' in info:
                    print(f"  Signature: {info['signature']}")
                if 'docstring' in info:
                    print(f"  Docstring: {info['docstring']}")
                if 'code' in info:
                    print(f"  Source Code:\n{info['code']}")
                print()
                if 'members' in info:
                    print("  Members:")
                    for member_name, member_info in info['members'].items():
                        print(f"    {member_name}:")
                        if 'type' in member_info:
                            print(f"      Type: {member_info['type']}")
                        if 'path' in member_info:
                            print(f"      Path: {member_info['path']}")
                        if 'signature' in member_info:
                            print(f"      Signature: {member_info['signature']}")
                        if 'docstring' in member_info:
                            print(f"      Docstring: {member_info['docstring']}")
                        if 'code' in member_info:
                            print(f"      Source Code:\n{member_info['code']}")
                        print()
        return 0
    except ImportError as e:
        print(f"Error: Module '{module_or_class}' not found. {str(e)}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return 1

if __name__ == '__main__':
    cli()
