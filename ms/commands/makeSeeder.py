import click
from flask.cli import with_appcontext
from .make import Make


@click.command(name='make:seeder',
               help='Create a new seeder class')
@click.option('-n', '--name', required=True, help='The name of the seeder')
@with_appcontext
def makeseeder(name):
    make = Make(
        entity_path="ms/db/seeders",
        template="seederTemplate.py"
    )

    make.set_entityname(name)

    if make.check():
        raise click.BadParameter(f"The file {make.filename} already exists")

    make.make(name)
