import threading

from olxoffercrawler.crawler import Crawler
from olxoffercrawler.config import read_urls

from webserver import server

urls = read_urls("URLS")
crawler = Crawler(urls)

threading.Timer(18000000, crawler.crawl).start()

server.run()
