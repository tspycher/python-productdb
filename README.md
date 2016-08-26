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