
from scrapping import BuckwheatInfo
from typing import Iterable, Mapping

def process(shops, sortkeyf=None, getf=None):
    if sortkeyf is None: sortkeyf = lambda bw: bw['price_per_kg']
    if getf is None: getf = lambda bws: bws

    return [
        {
            name: sorted(getf(list(jsonify(bws))), key=sortkeyf) for name, bws in shop.items()
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
