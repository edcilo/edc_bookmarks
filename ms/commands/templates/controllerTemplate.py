from flask import jsonify
from ms.controllers import Controller


class <CLASSNAME>(Controller):
    def index(self):
        response = {"foo": "bar"}
        return jsonify(response), 200
