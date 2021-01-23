from dataclasses import dataclass
from typing import Callable, Iterable
import re
import aiohttp

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


class BuckwheatInfoParser:
    WEIGHT_RE = re.compile(r'[0-9].*(?:г|кг|шт)')

    def __init__(self, url: str, get_info: Callable[[BeautifulSoup], Iterable[BuckwheatInfo]]):
        self.url = url
        self.get_info = get_info
        self.session = aiohttp.ClientSession()

    async def __del__(self):
        await self.session.close()

    # download and parse the goods
    async def parse(self) -> Iterable[BuckwheatInfo]:
        response = await self.session.get(self.url)
        bs = BeautifulSoup(await response.text(), 'html.parser')

        items = list(self.get_info(bs))
        for item in items:
            item.weight = self.process_weight(item.title if item.weight is None else item.weight)
            item.price = self.process_price(item.price)

        return items

    @staticmethod
    def process_weight(title):
        def units(s, sublst):
            for el in sublst:
                if el in s: return el

        def num(title):
            unit = units(title, ['шт', 'кг', 'г'])
            mult = { 'шт' : 1, 'кг' : 1, 'г' : 1e-3 }

            if unit is not None:
                return float(title.split(unit)[0].strip().replace(',', '.')) * mult[unit] 
            else:
                return float(title.strip().replace(',', '.'))

        expr = re.findall(r'[0-9].*(?:г|кг|шт)', title)[0].lower()
        mul = units(expr, ['*', 'x', 'х'])

        if mul is not None:
            a, b = expr.split(mul)
            return num(a) * num(b)
        else:
            return num(expr)

    @staticmethod
    def process_price(price):
        return float(price.replace(u'\xa0', u'').replace(' ', ''))
