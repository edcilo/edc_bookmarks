from .controller import Controller


class WebController(Controller):
    def index(self):
        return "hello from flask"
