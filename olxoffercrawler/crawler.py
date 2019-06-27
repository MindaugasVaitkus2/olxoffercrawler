from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from webserver.database import db_session
from webserver.models import OfferModel

import atexit


class Crawler(object):
    def __init__(self, start_urls=[]): 
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        self.driver = webdriver.Firefox(firefox_options=firefox_options)
        self.start_urls = start_urls

        atexit.register(self.quit)

    def quit(self):
        self.driver.quit()

    def get_element_or_empty(self, firefox_web_element, selector, attribute=None):
        try:
            element = firefox_web_element.find_element_by_css_selector(selector)
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

    def create_offer_model(self, firefox_web_element):
        url = self.get_element_or_empty(firefox_web_element, ".title-cell a", "href")
        title = self.get_element_or_empty(firefox_web_element, ".title-cell a")
        image = self.get_element_or_empty(firefox_web_element, ".thumb img", "src")
        price = self.get_element_or_empty(firefox_web_element, ".td-price p")
        location = self.get_element_or_empty(firefox_web_element, ".bottom-cell span")

        return OfferModel(url, title, image, price, location)

    def truncate_table(self):
        OfferModel.query.delete()
        
    def crawl(self):
        if not self.start_urls: 
            return None

        self.truncate_table()

        offers = []
        print(len(self.start_urls), "urls to crawl")
        for url in self.start_urls: 
            self.driver.get(url) 
            print("Crawl", url)

            pages = self.get_pages()
            
            print("Number of pages", len(pages))
            i = 1
            
            for page in pages:  
                self.driver.get(page)
                
                print("Page {0} of {1}".format(i, len(pages)))
                i += 1

                page_offers = self.driver.find_elements_by_class_name("offer")
                for offer in page_offers[:-1]:
                    offer_model = self.create_offer_model(offer) 

                    db_session.add(offer_model)
                    db_session.commit()
