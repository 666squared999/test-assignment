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

        yield BuckwheatInfo(title=title, url=url, photo_url=photo_url, price=price)


ROZETKA_URL = 'https://rozetka.com.ua/krupy/c4628397/sort=cheap;vid-225787=grechka/'
rozetka = BuckwheatInfoParser(ROZETKA_URL, rozetka_get_buckwheat)

##################################################
# novus-related stuff
##################################################


def novus_get_buckwheat(bs: BeautifulSoup) -> Iterable[BuckwheatInfo]:
    return []


NOVUS_URL = 'https://novus.zakaz.ua/ru/categories/buckwheat/?sort=price_asc'
novus = BuckwheatInfoParser(NOVUS_URL, novus_get_buckwheat)

##################################################
# auchan-related stuff
##################################################


def auchan_get_buckwheat(bs: BeautifulSoup) -> Iterable[BuckwheatInfo]:
    return []


AUCHAN_URL = 'https://auchan.zakaz.ua/uk/categories/buckwheat-auchan/?sort=price_asc'
auchan = BuckwheatInfoParser(AUCHAN_URL, auchan_get_buckwheat)

##################################################
# fozzyshop-related stuff
##################################################


def fozzyshop_get_buckwheat(bs: BeautifulSoup) -> Iterable[BuckwheatInfo]:
    return []


FOZZYSHOP_URL = 'https://fozzyshop.ua/ru/300143-krupa-grechnevaya?order=product.price.asc'
fozzyshop = BuckwheatInfoParser(FOZZYSHOP_URL, fozzyshop_get_buckwheat)
