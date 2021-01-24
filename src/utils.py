
from typing import Iterable, Mapping, Callable, Optional, Awaitable
from functools import wraps
import asyncio

from scrapping import BuckwheatInfo


def process(shops, sortkeyf=None, getf=None):
    if sortkeyf is None: sortkeyf = lambda bw: bw['price_per_kg']
    if getf is None: getf = lambda bws: bws

    return [
        {
            name: getf(sorted(list(jsonify(bws)), key=sortkeyf)) for name, bws in shop.items()
        } 
        for shop in shops
    ]


def jsonify(bws: Iterable[BuckwheatInfo]) -> Iterable[Mapping]:
    for bw in bws:
        yield {
            'title': bw.title,
            'weight': bw.weight,
            'price_per_kg': bw.price / bw.weight,
            'photo_url': bw.photo_url,
            'page_url': bw.url
        }

async def parse(rozetka, fozzyshop, novus, auchan):
    return [
        { 'rozetka': await rozetka.parse() },
        { 'fozzyshop': await fozzyshop.parse() },
        { 'novus': await novus.parse() },
        { 'auchan': await auchan.parse() },
    ]
    