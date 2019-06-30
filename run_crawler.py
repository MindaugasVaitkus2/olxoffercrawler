from apscheduler.schedulers.background import BackgroundScheduler 

from olxoffercrawler.crawler import Crawler
from olxoffercrawler.config import read_urls

sched = BackgroundScheduler()

@sched.scheduled_job("interval", hours=5)
def start_crawler():
    urls = read_urls("URLS")
    crawler = Crawler(urls)
    crawler.crawl()    

sched.start()
