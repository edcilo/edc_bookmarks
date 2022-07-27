import click
from flask.cli import with_appcontext
from .make import Make


@click.command(name='make:form',
               help='Create a new form class')
@click.option("-n", "--name", required=True, help="The name of the form")
@with_appcontext
def makeform(name):
    make = Make(
        entity_path="ms/forms",
        template="formTemplate.py"
    )

    make.set_entityname(name)

    if make.check():
        raise click.BadParameter(f"The file {make.filename} already exists")

    make.make(name)
