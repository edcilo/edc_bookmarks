from ms import app
from .autopep8 import pep8
from .makeController import makecontroller
from .makeForm import makeform
from .makeMiddleware import makemiddleware
from .makeModel import makemodel
from .makeRepository import makerepository
from .makeSeeder import makeseeder
from .makeSerializer import makeserializer


app.cli.add_command(pep8)
app.cli.add_command(makecontroller)
app.cli.add_command(makeform)
app.cli.add_command(makemiddleware)
app.cli.add_command(makemodel)
app.cli.add_command(makerepository)
app.cli.add_command(makeseeder)
app.cli.add_command(makeserializer)
