import click
from flask.cli import with_appcontext
from .make import Make


@click.command(name='make:controller',
               help='Create a new controller class')
@click.option("-n", "--name", required=True, help="The name of the class")
@with_appcontext
def makecontroller(name):
    make = Make(
        entity_path="ms/controllers",
        template="controllerTemplate.py"
    )

    make.set_entityname(name)

    if make.check():
        raise click.BadParameter(f"The file {make.filename} already exists")

    make.make(name)
