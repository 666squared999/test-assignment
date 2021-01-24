from fastapi import FastAPI
import asyncio

from scrapping import get_rozetka, get_fozzyshop, get_novus, get_auchan, BuckwheatInfo

import utils

app = FastAPI()
rozetka, fozzyshop, novus, auchan = get_rozetka(), get_fozzyshop(), get_novus(), get_auchan()

@app.get("/buckwheat")
async def bw(wmin: float = None, wmax: float = None, allres: bool = False):
    shops = await utils.parse(rozetka, fozzyshop, novus, auchan)

    getf = (lambda bws: bws[:1]) if allres is False else (lambda bws: bws)
    wmin = 0.0 if wmin is None else wmin
    wmax = float('inf') if wmax is None else wmax

    return utils.process(shops, getf=lambda bws: getf(
        [bw for bw in bws if wmin <= bw['weight'] <= wmax]
    ))
