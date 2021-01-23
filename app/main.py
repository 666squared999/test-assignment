from fastapi import FastAPI
from scrapping import rozetka, fozzyshop, novus, auchan

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/buckwheat")
async def bw():
    return [
        {
            'rozetka' : [el.__dict__ for el in rozetka.parse()],
            'fozzyshop' : [el.__dict__ for el in fozzyshop.parse()],
            'novus' : [el.__dict__ for el in novus.parse()],
            'auchan' : [el.__dict__ for el in auchan.parse()],
        }
    ]