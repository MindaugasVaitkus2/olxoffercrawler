from offercrawler.crawler import Crawler
from offercrawler.config import read_urls

urls = read_urls("URLS")
crawler = Crawler(urls)
crawler.crawl()    
