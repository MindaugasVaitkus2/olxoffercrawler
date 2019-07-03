from webserver import application
from flask import(
    render_template 
)

from webserver.database import db_session
from webserver.models import OfferModel

from offercrawler.logger import Logger


@application.route("/", methods=["GET", "POST"])
def index():	
    offers = OfferModel.query.all()	
    last_run = Logger.get_last_run()
    return render_template("index.html", offers=offers, last_run=last_run)
