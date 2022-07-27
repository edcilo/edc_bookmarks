import click
from flask.cli import with_appcontext
from .make import Make


@click.command(name='make:serializer',
               help='Create a new serializer class')
@click.option('-n', '--name', required=True, help='The name of the serializer')
@with_appcontext
def makeserializer(name):
    make = Make(
        entity_path="ms/serializers",
        template="serializerTemplate.py"
    )

    make.set_entityname(name)

    if make.check():
        raise click.BadParameter(f"The file {make.filename} already exists")

    make.make(name)
