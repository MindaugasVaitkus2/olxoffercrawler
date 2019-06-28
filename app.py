import threading

from olxoffercrawler.crawler import Crawler
from olxoffercrawler.config import read_urls

from webserver import server

def run_crawler_and_start_new_timer():    
    urls = read_urls("URLS")
    crawler = Crawler(urls)
    threading.timer(18000000, crawler.crawl).start()

threading.Timer(18000000, run_crawler_and_start_new_timer).start()

if __name__ == '__main__':
	import os
	port = int(os.environ.get('PORT', 5000))
	server.run(host="0.0.0.0", port=port)
