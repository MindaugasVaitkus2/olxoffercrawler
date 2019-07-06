from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from urllib.parse import urljoin

from webserver.database import db_session
from webserver.models import OfferModel

from offercrawler.logger import Logger

import atexit
import re


class Crawler(object):
    def __init__(self, start_urls=[]): 
        self.driver = webdriver.PhantomJS(executable_path=r"phantomjs/phantomjs")
        self.start_urls = start_urls

        atexit.register(self.quit)

    def quit(self):
        self.driver.quit()

    def get_element_or_empty(self, phantomjs_web_element, selector, attribute=None):
        try:
            element = phantomjs_web_element.find_element_by_css_selector(selector)
            return element.text if not attribute else element.get_attribute(attribute)
        except NoSuchElementException:
            return ""

    def get_pages(self):
        pager = self.driver.find_element_by_css_selector(".pager")
        items = pager.find_elements_by_class_name("item")
        
        pages = [] 
        for item in items[:-1]:
            try:
                page = item.find_element_by_tag_name("a").get_attribute("href")
                pages.append(page)
            except NoSuchElementException:
                pass

        return pages

    def create_offer_model(self, phantomjs_web_element):
        url = self.get_element_or_empty(phantomjs_web_element, ".title-cell a", "href")
        title = self.get_element_or_empty(phantomjs_web_element, ".title-cell a")
        image = self.get_element_or_empty(phantomjs_web_element, ".thumb img", "src")
        price = self.get_element_or_empty(phantomjs_web_element, ".td-price p")
        location = self.get_element_or_empty(phantomjs_web_element, ".bottom-cell span")

        price = int(re.sub("[^0-9]", "", price))

        return OfferModel(url, title, image, price, location)

    def truncate_table(self):
        OfferModel.query.delete()
        
    def crawl(self):
        if not self.start_urls: 
            return None

        self.truncate_table()
 
        print("{0} urls to crawl".format(len(self.start_urls)))

        offers = []
        for url in self.start_urls: 
            self.driver.get(url)

            print("Crawl {0}".format(url))
            
            pages = self.get_pages()
             
            print("Number of pages {0}".format(len(pages)))
            i = 1
           
            page_offers_sum = 0 
            for page in pages:  
                self.driver.get(page)
                
                print("Page {0} of {1}".format(i, len(pages)), end="\t")
                i += 1

                page_offers = self.driver.find_elements_by_class_name("offer")
                print("collecting {0} elements".format(len(page_offers)))
                page_offers_sum += len(page_offers)
                for offer in page_offers[:-1]:
                    offers.append(self.create_offer_model(offer)) 
                    
            print("Done! Collected {0} elements".format(page_offers_sum))
 
        offers = list(set(offers))

        print("{0} elements after remove duplicates".format(len(offers)))

        db_session.add_all(offers)
        db_session.commit() 
        
        Logger.save_last_run()
