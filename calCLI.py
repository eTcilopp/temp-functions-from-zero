#!/usr/bin/env python3

from mylib.calc import add, subtract, multiply, divide
import click


@click.group()
def cli():
    """Command line interface for the calculator."""


@cli.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def add_command(a, b):
    """Add two numbers."""
    click.echo(add(a, b))


@cli.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def subtract_command(a, b):
    """Subtract two numbers."""
    click.echo(subtract(a, b))


@cli.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def multiply_command(a, b):
    """Multiply two numbers."""
    click.echo(multiply(a, b))


@cli.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def divide_command(a, b):
    """Divide two numbers."""
    click.echo(divide(a, b))


if __name__ == "__main__":
    cli()
