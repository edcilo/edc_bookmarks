from flask import abort
from .middleware import Middleware


class <CLASSNAME>(Middleware):
    def handler(self, request):
        if True:
            abort(403)
        return True
