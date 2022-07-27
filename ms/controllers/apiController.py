from flask import jsonify
from ms import app
from .controller import Controller


class ApiController(Controller):
    def index(self):
        return jsonify({
            "app_name": app.config.get("APP_NAME"),
            "version": app.config.get("APP_VERSION")
        }), 200
