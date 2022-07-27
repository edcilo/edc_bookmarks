import click
import re
from flask.cli import with_appcontext
from .make import Make


class MakeModel(Make):
    @property
    def placeholders(self):
        return [
            {
                'placeholder': '<CLASSNAME>',
                'value': 'entityName',
            },
            {
                'placeholder': '<TABLENAME>',
                'value': 'tableName',
            }
        ]

    @property
    def tableName(self):
        return re.sub(r'(?<!^)(?=[A-Z])', '_', self.entityName).lower()


@click.command(name='make:model',
               help='Create a new model class')
@click.option('-n', '--name', required=True, help='The name of the class')
@with_appcontext
def makemodel(name):
    make = MakeModel(
        entity_path="ms/models",
        template="modelTemplate.py"
    )

    make.set_entityname(name)

    if make.check():
        raise click.BadParameter(f"The file {make.filename} already exists")

    make.make(name)
