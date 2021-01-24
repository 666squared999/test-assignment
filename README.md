# Backend test assignment [![Build Status](http://34.123.0.188:8080/job/Deployment%20Job/badge/icon)](http://34.123.0.188:8080/job/Deployment%20Job/)

This is our solution to the test assignment of `int20h` hackathon. The task description is [here](https://mcusercontent.com/a90be75a5d6a2bb92a394e975/files/58c87f07-4fd7-4ec9-9119-456d8558f0b3/web_task.pdf) 

* [api server](https://api-grechka.ml/)
* [api docs(swagger)](https://api-grechka.ml/docs)
* [api docs(redoc)](https://api-grechka.ml/redoc)

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
# minimal acceptable weight of the buckwheat
wmin: float = 0.0 

# maxmal  acceptable weight of the buckwheat
wmax: float = inf

# should we display ALL RESults sorted by smallest price/kg?
# if default, returns only one cheapest option from each shop
# in according weight ranges
allres: float = False 
```
