from ms.controllers import WebController
from .blueprints import web


@web.route("/")
def index():
    return WebController.action('index')
