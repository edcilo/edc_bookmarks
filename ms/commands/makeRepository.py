import click
from flask.cli import with_appcontext
from .make import Make


@click.command(name='make:repository',
               help='Create a new repository class')
@click.option('-n', '--name', required=True, help='The name of the class')
@with_appcontext
def makerepository(name):
    make = Make(
        entity_path="ms/repositories",
        template="repositoryTemplate.py"
    )

    make.set_entityname(name)

    if make.check():
        raise click.BadParameter(f"The file {make.filename} already exists")

    make.make(name)
