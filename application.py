from apscheduler.schedulers.background import BackgroundScheduler 

from olxoffercrawler.crawler import Crawler
from olxoffercrawler.config import read_urls
from webserver import server

import atexit

sched = BackgroundScheduler()

@sched.scheduled_job('interval', hours=5)
def run_crawler():
    urls = read_urls("URLS")
    crawler = Crawler(urls)
    crawler.crawl()    

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    sched.start()
    server.run(host="0.0.0.0", port=port, threaded=True)

