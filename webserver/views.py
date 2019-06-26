from webserver import server
from flask import(
    render_template 
)

from webserver.database import db_session
from webserver.models import OfferModel


@server.route("/", methods=["GET", "POST"])
def index():	
	offers = OfferModel.query.all()	
	return render_template("index.html", offers=offers)
