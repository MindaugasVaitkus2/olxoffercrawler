from apscheduler.schedulers.background import BackgroundScheduler 

from offercrawler.crawler import Crawler
from offercrawler.config import read_urls
from webserver import application 

import atexit

sched = BackgroundScheduler()

@sched.scheduled_job('interval', hours=5)
def run_crawler():
    urls = read_urls("URLS")
    crawler = Crawler(urls)
    crawler.crawl()    

if __name__ == '__main__': 
    sched.start() 
    application.run()
   
