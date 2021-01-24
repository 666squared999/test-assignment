from typing import Callable, Iterable

from bs4 import BeautifulSoup

from .parser import BuckwheatInfo, BuckwheatInfoParser


##################################################
# rozetka-related stuff
##################################################


def rozetka_get_buckwheat(bs: BeautifulSoup) -> Iterable[BuckwheatInfo]:
    available_items = bs.select('div[class="goods-tile"]')
    for item in available_items:
        heading = item.select_one('a[class="goods-tile__heading"]')

        title = heading['title'].strip()
        url = heading['href']

        photo_url = item.select_one('a').contents[1]['src']
        price = item.select_one(
            'span[class="goods-tile__price-value"]').text.strip()

        yield BuckwheatInfo(title, url, photo_url, price)


ROZETKA_URL = 'https://rozetka.com.ua/krupy/c4628397/sort=cheap;vid-225787=grechka/'
def get_rozetka(): return BuckwheatInfoParser(ROZETKA_URL, rozetka_get_buckwheat)


##################################################
# fozzyshop-related stuff
##################################################


def fozzyshop_get_buckwheat(bs: BeautifulSoup) -> Iterable[BuckwheatInfo]:
    items = bs.find_all('div', class_='js-product-miniature-wrapper')
    for item in items:
        header = item.select_one('a')
        title, url = header.img['alt'], header['href']
        photo_url = header.img['src']
        price = item.select_one('span[class="product-price"]')['content']
        weight = item.select_one('div[class="product-reference text-muted"]').a.string
        yield BuckwheatInfo(title, url, photo_url, price, weight)

FOZZYSHOP_URL = 'https://fozzyshop.ua/ru/300143-krupa-grechnevaya?order=product.price.asc'
def get_fozzyshop(): return BuckwheatInfoParser(FOZZYSHOP_URL, fozzyshop_get_buckwheat)


##################################################
# zakaz.ua-related stuff
# (a common platform for all of the below)
##################################################


def zakazua_get_buckwheat(shop: str):
    def _(bs: BeautifulSoup) -> Iterable[BuckwheatInfo]:
        items = bs.find_all('div', class_='products-box__list-item')
        for item in items:
            title = item.select_one('a')['title']
            url = r'https://' + shop + r'.zakaz.ua' + item.select_one('a')['href']
            photo_url = item.select_one('a > div > img')['src']
            price = item.find('span', class_='Price__value_caption').text
            weight = item.find('div', class_='product-tile__weight').string
            yield BuckwheatInfo(title, url, photo_url, price, weight)
    
    return _



##################################################
# novus-related stuff
##################################################


NOVUS_URL = 'https://novus.zakaz.ua/ru/categories/buckwheat/?sort=price_asc'
def get_novus(): return BuckwheatInfoParser(NOVUS_URL, zakazua_get_buckwheat(r'novus'))


##################################################
# auchan-related stuff
##################################################


AUCHAN_URL = 'https://auchan.zakaz.ua/uk/categories/buckwheat-auchan/?sort=price_asc'
def get_auchan(): return BuckwheatInfoParser(AUCHAN_URL, zakazua_get_buckwheat(r'auchan'))

