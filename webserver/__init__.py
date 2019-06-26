from flask import(
    Flask,
    render_template
)

server = Flask(__name__)

from webserver.database import init_database
init_database()

import webserver.views
