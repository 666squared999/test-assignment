import pytest

from utils import process, jsonify
from scrapping import BuckwheatInfo

def test_process():
    shops = [
        {
            'ashop' : [
                BuckwheatInfo('a', 'a', 'a', 5, 1), 
                BuckwheatInfo('aa', 'aa', 'aa', 5, 2), 
                BuckwheatInfo('aaa', 'aaa', 'aaa', 5, 4),
            ]
        },
        { 
            'bshop' : [
                BuckwheatInfo('b', 'b', 'b', 10, 1),
                BuckwheatInfo('bb', 'bb', 'bb', 10, 2),
                BuckwheatInfo('bbb', 'bbb', 'bbb', 10, 4),
            ]
        }
    ]

    keyf = lambda bw: 1 / bw['weight'] 
    getf = lambda bws: [bws[-1]]

    print(process(shops, keyf, getf))

    assert process(shops, keyf, getf) == [
        {
            'ashop' : [{
                'title': 'a',
                'weight': 1,
                'price_per_kg': 5,
                'photo_url': 'a',
                'page_url': 'a'
            }]
        },
        {
            'bshop' : [{
                'title': 'b',
                'weight': 1,
                'price_per_kg': 10,
                'photo_url': 'b',
                'page_url': 'b'
            }]
        },
    ]
