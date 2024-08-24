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
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.markdown import Markdown

def cli(module_or_class, depth, sigs, docs, code, imports, all, markdown):
    """Inspect a Python module or class. Optionally create a markdown file."""
    console = Console()
    try:
        result = inspect_library(module_or_class, depth, sigs, docs, code, imports, all, markdown)
    
        if markdown:
            md_content = "# Inspection Result\n\n"
            for name, info in result.items():
                md_content += f"## {name}\n\n"
                if 'type' in info:
                    md_content += f"**Type:** {info['type']}\n\n"
                if 'path' in info:
                    md_content += f"**Path:** {info['path']}\n\n"
                if 'signature' in info:
                    md_content += f"**Signature:**\n```python\n{info['signature']}\n```\n\n"
                if 'docstring' in info:
                    md_content += f"**Docstring:**\n```\n{info['docstring']}\n```\n\n"
                if 'code' in info:
                    md_content += f"**Source Code:**\n```python\n{info['code']}\n```\n\n"
                if 'members' in info:
                    md_content += "### Members\n\n"
                    for member_name, member_info in info['members'].items():
                        md_content += f"#### {member_name}\n\n"
                        if 'type' in member_info:
                            md_content += f"**Type:** {member_info['type']}\n\n"
                        if 'path' in member_info:
                            md_content += f"**Path:** {member_info['path']}\n\n"
                        if 'signature' in member_info:
                            md_content += f"**Signature:**\n```python\n{member_info['signature']}\n```\n\n"
                        if 'docstring' in member_info:
                            md_content += f"**Docstring:**\n```\n{member_info['docstring']}\n```\n\n"
                        if 'code' in member_info:
                            md_content += f"**Source Code:**\n```python\n{member_info['code']}\n```\n\n"
            console.print(Markdown(md_content))
        else:
            for name, info in result.items():
                panel_content = f"[bold cyan]{name}[/bold cyan]\n\n"
                if 'type' in info:
                    panel_content += f"[bold]Type:[/bold] {info['type']}\n"
                if 'path' in info:
                    panel_content += f"[bold]Path:[/bold] {info['path']}\n"
                if sigs and 'signature' in info:
                    panel_content += f"\n[bold]Signature:[/bold]\n{Syntax(info['signature'], 'python', theme='monokai')}\n"
                if docs and 'docstring' in info:
                    panel_content += f"\n[bold]Docstring:[/bold]\n{info['docstring']}\n"
                if code and 'code' in info:
                    panel_content += f"\n[bold]Source Code:[/bold]\n{Syntax(info['code'], 'python', theme='monokai')}\n"
                
                console.print(Panel(panel_content, expand=False))
                
                if 'members' in info:
                    console.print("\n[bold]Members:[/bold]")
                    for member_name, member_info in info['members'].items():
                        member_panel = f"[bold cyan]{member_name}[/bold cyan]\n\n"
                        if 'type' in member_info:
                            member_panel += f"[bold]Type:[/bold] {member_info['type']}\n"
                        if 'path' in member_info:
                            member_panel += f"[bold]Path:[/bold] {member_info['path']}\n"
                        if sigs and 'signature' in member_info:
                            member_panel += f"\n[bold]Signature:[/bold]\n{Syntax(member_info['signature'], 'python', theme='monokai')}\n"
                        if docs and 'docstring' in member_info:
                            member_panel += f"\n[bold]Docstring:[/bold]\n{member_info['docstring']}\n"
                        if code and 'code' in member_info:
                            member_panel += f"\n[bold]Source Code:[/bold]\n{Syntax(member_info['code'], 'python', theme='monokai')}\n"
                        
                        console.print(Panel(member_panel, expand=False))
        return 0
    except ImportError as e:
        console.print(f"[bold red]Error:[/bold red] Module '{module_or_class}' not found. {str(e)}", style="red")
        return 1
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}", style="red")
        return 1

if __name__ == '__main__':
    cli()
