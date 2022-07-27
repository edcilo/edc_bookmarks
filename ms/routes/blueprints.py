from flask import Blueprint


api = Blueprint('api', __name__, url_prefix="/api/v1")
web = Blueprint('web', __name__, url_prefix="/")
