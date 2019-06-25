from olxflatcrawler.crawler import Crawler
from olxflatcrawler.config import OLX_URLS

flatcrawler = Crawler()
flatcrawler.start_urls = OLX_URLS

flats = flatcrawler.crawl()

for flat in flats:
    print(flat)
