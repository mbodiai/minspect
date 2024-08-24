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
