# python-productdb
A little playground for a python project with flask/eve

installation

```
virtualenv ./venv
. venv/bin/activate
pip install -r REQUIREMENTS.txt
```

To run the Webserver from projectroot

```PYTHONPATH=. python productdb/run.py```

To import the feed.xml

```PYTHONPATH=. python productdb/manage.py readfeed -f data/feed.xml```


The Api is available under http://localhost:5000/ and http://localhost:5000/product and allows GET, POST, PUT, PATCH, DELETE
A pretty simple HTML/Angular Webapp is available under http://localhost:5000/web/index.html

To get a specific item "search" for it with the following url: http://127.0.0.1:5000/product?where={"code": "879891"}

Directly access an item with either its code http://localhost:5000/product/<CODE> or mongo ID http://localhost:5000/product/<OBJECTID>

# Missing features
 * Pagination on Frontend
 * CRUD Operations on Frontend
 * Search implementation with ElasticSearch