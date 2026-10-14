from mylib.calc import *
from calCLI import cli
from click.testing import CliRunner
from pytest import fixture

@fixture
def runner():
    return CliRunner()

def test_add_command(runner):
    result = runner.invoke(cli, ["add-command", "2", "3"])
    assert result.exit_code == 0
    assert "5" in result.output


def test_subtract_command(runner):
    result = runner.invoke(cli, ["subtract-command", "5", "3"])
    assert result.exit_code == 0
    assert "2" in result.output

def test_multiply_command(runner):
    result = runner.invoke(cli, ["multiply-command", "2", "3"])
    assert result.exit_code == 0
    assert "6" in result.output


def test_divide_command(runner):
    result = runner.invoke(cli, ["divide-command", "6", "3"])
    assert result.exit_code == 0
    assert "2" in result.output

# write a test for help command
def test_help_command(runner):
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "Command line interface for the calculator." in result.output
    assert "add-command" in result.output
    assert "subtract-command" in result.output
    assert "multiply-command" in result.output
    assert "divide-command" in result.output
    assert "--help" in result.output

