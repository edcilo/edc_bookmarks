from ms.controllers import ApiController
from .blueprints import api


@api.route('/')
def api_index():
    return ApiController.action('index')
