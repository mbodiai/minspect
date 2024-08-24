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
    print(result)

if __name__ == '__main__':
    cli()
