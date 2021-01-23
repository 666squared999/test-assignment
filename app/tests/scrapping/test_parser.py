import pytest

from scrapping import BuckwheatInfoParser


def test_process_price():
    input = [u'2\xa002.23', '202.23', '202,23', '2 0 2 , 2 3']
    assert all([BuckwheatInfoParser.process_price(el) == 202.23 for el in input])

def test_process_weight():
    input = """1 кг
        250 г
        500г
        4 х 100 г
        50кг
        800 г х 5 шт
        1,0 кг
        за 1 кг
        5*80г
        400г х16""".split('\n')
    results = [1, 0.25, 0.5, 0.4, 50, 4, 1, 1, 0.4, 6.4]

    assert [BuckwheatInfoParser.process_weight(el) for el in input] == results
