from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from olxflatcrawler.flat import Flat 

import atexit


class Crawler(object):
    def __init__(self): 
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        self.driver = webdriver.Firefox(firefox_options=firefox_options)
        self.start_urls = []

        atexit.register(self.quit)

    def quit(self):
        self.driver.quit()

    def get_element_or_empty(self, firefox_web_element, selector, attribute=None):
        try:
            element = firefox_web_element.find_element_by_css_selector(selector)
            return element.text if not attribute else element.get_attribute(attribute)
        except NoSuchElementException:
            return ""

    def create_flat(self, firefox_web_element):
        url = self.get_element_or_empty(firefox_web_element, ".title-cell a", "href")
        title = self.get_element_or_empty(firefox_web_element, ".title-cell a")
        image = self.get_element_or_empty(firefox_web_element, ".thumb img", "src")
        price = self.get_element_or_empty(firefox_web_element, ".td-price p")

        return Flat(url, title, image, price)

    def crawl(self):
        if not self.start_urls:
            return

        flats = []
        for url in self.start_urls:
            self.driver.get(url) 

            offers = self.driver.find_elements_by_class_name("offer")
            for offer in offers:
                flat = self.create_flat(offer) 
                flats.append(flat)     
        
        return flats
       
