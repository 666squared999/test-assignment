from dataclasses import dataclass
from typing import Callable, Iterable
import re

from bs4 import BeautifulSoup
from requests import Response
import requests



@dataclass
class BuckwheatInfo:
    title: str
    url: str
    photo_url: str

    # will be set properly on return from BuckwheatInfoParser.parse
    price: float   = None # in hryvnias
    weight: float  = None # in kilograms



@dataclass
class BuckwheatInfoParser:
    WEIGHT_RE = re.compile(r'[0-9].*(?:г|кг|шт)')

    url: str
    get_info: Callable[[BeautifulSoup], Iterable[BuckwheatInfo]]
    page: Response = None

    def parse(self) -> Iterable[BuckwheatInfo]:
        if self.page is None:
            self.page = requests.get(self.url)
        
        bs = BeautifulSoup(self.page.content, 'html.parser')

        items = list(self.get_info(bs))
        for item in items:
            item.weight = self.process_weight(item.title)
            item.price = self.process_price(item.price)

        return items

    @staticmethod
    def process_weight(title):
        expr = re.findall(BuckwheatInfoParser.WEIGHT_RE, title)
        return expr

    @staticmethod
    def process_price(price):
        return price
