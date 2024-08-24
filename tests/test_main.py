from click.testing import CliRunner
from minspect.main import cli

def test_cli():
    runner = CliRunner()
    result = runner.invoke(cli, ["minspect", "--depth", "1"])
    assert result.exit_code == 0
    assert "minspect" in result.output

def test_cli_with_options():
    runner = CliRunner()
    result = runner.invoke(cli, ["minspect", "--depth", "1", "--sigs", "--docs"])
    assert result.exit_code == 0
    assert "minspect" in result.output
    assert "Signature:" in result.output
    assert "Docstring:" in result.output
    assert "Type:" in result.output
    assert "Path:" in result.output
    assert "Members:" in result.output

def test_cli_with_sigs():
    runner = CliRunner()
    result = runner.invoke(cli, ["minspect", "--sigs"])
    assert result.exit_code == 0
    assert "Signature:" in result.output

def test_cli_with_docs():
    runner = CliRunner()
    result = runner.invoke(cli, ["minspect", "--docs"])
    assert result.exit_code == 0
    assert "Docstring:" in result.output

def test_cli_with_code():
    runner = CliRunner()
    result = runner.invoke(cli, ["minspect", "--code"])
    assert result.exit_code == 0
    assert "Source code:" in result.output

def test_cli_with_imports():
    runner = CliRunner()
    result = runner.invoke(cli, ["minspect", "--imports"])
    assert result.exit_code == 0
    # Add an appropriate assertion for imports

def test_cli_with_all():
    runner = CliRunner()
    result = runner.invoke(cli, ["minspect", "--all"])
    assert result.exit_code == 0
    assert "Signature:" in result.output
    assert "Docstring:" in result.output
    assert "Source code:" in result.output
    # Add an appropriate assertion for imports

def test_cli_with_markdown():
    runner = CliRunner()
    result = runner.invoke(cli, ["minspect", "--markdown"])
    assert result.exit_code == 0
    assert "```python" in result.output  # Assuming markdown output includes code blocks

def test_cli_with_multiple_options():
    runner = CliRunner()
    result = runner.invoke(cli, ["minspect", "--depth", "2", "--sigs", "--docs", "--code"])
    assert result.exit_code == 0
    assert "Signature:" in result.output
    assert "Docstring:" in result.output
    assert "Source code:" in result.output
    assert "Members:" in result.output

# Add more tests for other combinations as needed
