from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
# TODO: add restriction by origin , origins=["http://localhost:3000"]
CORS(app)


import ms.config
import ms.commands
import ms.db
import ms.models
import ms.routes
