import threading

from olxoffercrawler.crawler import Crawler
from olxoffercrawler.config import read_urls

from webserver import server

def run_crawler_and_start_new_timer():    
    urls = read_urls("URLS")
    crawler = Crawler(urls)
    threading.timer(18000000, crawler.crawl).start()

threading.Timer(18000000, run_crawler_and_start_new_timer).start()

server.run()
