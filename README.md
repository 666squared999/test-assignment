# Backend test assignment [![Build Status](http://34.123.0.188:8080/job/Deployment%20Job/badge/icon)](http://34.123.0.188:8080/job/Deployment%20Job/)

This is our solution to the test assignment of `int20h` hackathon. The task description is [here](https://mcusercontent.com/a90be75a5d6a2bb92a394e975/files/58c87f07-4fd7-4ec9-9119-456d8558f0b3/web_task.pdf) 

* [api server](https://api-grechka.ml/)
* [api docs(swagger)](https://api-grechka.ml/docs)
* [api docs(redoc)](https://api-grechka.ml/redoc)

# Example

```
# Requeslt URL
https://api-grechka.ml/buckwheat?wmin=2&wmax=60&allres=true

# Result json
[
  {
    "rozetka": [
      {
        "title": "Гречневая крупа в мешках 50кг ТМ \"Хатинка\"",
        "weight": 50,
        "price_per_kg": 40.4,
        "photo_url": "https://i8.rozetka.ua/goods/21254626/271080001_images_21254626536.jpg",
        "page_url": "https://rozetka.com.ua/ua/271080001/p271080001/"
      },
      {
        "title": "Упаковка крупи гречаної ядриця Терра першого сорту 800 г х 5 шт. (4820015737045)",
        "weight": 4,
        "price_per_kg": 72.75,
        "photo_url": "https://i8.rozetka.ua/goods/14351951/terra_4820015737045_images_14351951423.jpg",
        "page_url": "https://rozetka.com.ua/ua/terra_4820015737045/p128496331/"
      },
      {
        "title": "Упаковка крупи гречаної зеленої ядриця Терра першого сорту 800 г х 5 шт. (4820015737052)",
        "weight": 4,
        "price_per_kg": 83.75,
        "photo_url": "https://i8.rozetka.ua/goods/14352153/terra_4820015737052_images_14352153170.jpg",
        "page_url": "https://rozetka.com.ua/ua/terra_4820015737052/p128510905/"
      },
      {
        "title": "Упаковка крупи гречаної ядриця Терра першого сорту швидкого приготування у варильному пакеті 400 г х 5 шт. (4820015737281)",
        "weight": 2,
        "price_per_kg": 114.5,
        "photo_url": "https://i2.rozetka.ua/goods/14352296/terra_4820015737281_images_14352296089.jpg",
        "page_url": "https://rozetka.com.ua/ua/terra_4820015737281/p128516463/"
      }
    ]
  },
  {
    "fozzyshop": []
  },
  {
    "novus": []
  },
  {
    "auchan": []
  }
]
```

# HOWTO run

```
# builds and runs server
docker-compose up 

# runs tests
# (works only if previous step was done at least once)
# (e.g. the container was build)
docker run -it api-grechka tests
```

# HOWTO query

It's very simple API consisting of one endpoint `/buckwheat`. 
There are three optional parameters:

```
# minimal acceptable weight of the buckwheat in kg
wmin: float = 0.0 

# maxmal  acceptable weight of the buckwheat in kg
wmax: float = inf

# should we display ALL RESults sorted by smallest price/kg?
# if default, returns only one cheapest option from each shop
# in according weight ranges
allres: float = False 
```

