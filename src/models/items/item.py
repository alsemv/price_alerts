import requests
from bs4 import BeautifulSoup
import re
import src.models.items.constants as ItemConstants
from src.common.database import Database


class Item(object):
    def __init__(self, name, url, store):
        self.name = name
        tag_name = store.tag_name
        query = store.query
        self.price = self.load_price(tag_name, query)
        self.url = url
        self.store = store

    def __repr__(self):
        return "<Item {} with URL {}>".format(self.name, self.url)

    def load_price(self, tag_name, query):
        #<span id="priceblock_ourprice" class="a-size-medium a-color-price">$13.99</span>

        request = requests.get(self.url)
        content = request.content
        soup = BeautifulSoup(content, "html.parser")
        element = soup.find(tag_name, query)
        string_price = element.text.strip()

        pattern = re.compile("(\d+.\d+)")
        match = pattern.search(string_price)
        return match.group()

    def save_to_mongo(self):
        Database.insert(ItemConstants.COLLECTION, self.json())

    def json(self):
        return {
            "name": self.name,
            "url": self.url
        }