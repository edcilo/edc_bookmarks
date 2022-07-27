import click
import os
from flask.cli import with_appcontext


@click.command(name='pep8',
               help='Automatically formats Python code to conform to the PEP 8 Style guide.')
@click.option("-p", "--path", default="./ms", help="folder path to fix code")
@with_appcontext
def pep8(path):
    os.system(f"autopep8 {path}")
