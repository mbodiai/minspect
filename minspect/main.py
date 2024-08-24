from click import argument, command, option, help_option

from minspect.inspecting import inspect_library


@command("minspect")
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
    result = inspect_library(module_or_class, depth, sigs, docs, code, imports, all, markdown)
    for name, info in result.items():
        print(f"{name}:")
        if 'type' in info:
            print(f"  Type: {info['type']}")
        if 'path' in info:
            print(f"  Path: {info['path']}")
        if 'signature' in info:
            print(f"  Signature: {info['signature']}")
        if 'docstring' in info:
            print(f"  Docstring: {info['docstring'][:50]}...")
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
                    print(f"      Docstring: {member_info['docstring'][:50]}...")
                print()

if __name__ == '__main__':
    cli()
