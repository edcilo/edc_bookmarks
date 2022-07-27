from ms import app
from .web import web
from .api import api


app.register_blueprint(web)
app.register_blueprint(api)
