from webserver import server
from flask import(
    render_template 
)


@server.route("/", methods=["GET", "POST"])
def index():
	return render_template("index.html")
