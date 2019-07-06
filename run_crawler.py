from olxoffercrawler.crawler import Crawler
from olxoffercrawler.config import read_urls

urls = read_urls("URLS")
crawler = Crawler(urls)
crawler.crawl()    
