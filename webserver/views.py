from webserver import server
from flask import(
    render_template 
)

from olxflatcrawler.crawler import Crawler
from olxflatcrawler.config import OLX_URLS


@server.route("/", methods=["GET", "POST"])
def index():
	crawler = Crawler(OLX_URLS)
	flats = crawler.crawl()
	return render_template("index.html", flats=flats)
