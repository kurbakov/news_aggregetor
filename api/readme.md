## API documentation

The API is based on the Flask framework. For the API dependencies please check the file with all dependencies.

### How to run API

As it is a stundard Flask framework you just need to execute the run_api.py

```bash
python run_api.py
```
Also there are a lot of setup oportunities. For more information please see the Flask [documentation](http://flask.pocoo.org/docs/0.12/).

### Methods

Sinse the APP is very basic we need only one method for API: full text search.

## GET /search

The search method takes only 1 argument the search string.
you can use the method as the following GET request:
```bash
curl -XGET http://127.0.0.1:5000/api/v1/search?q=TEXT
```
where TEXT is our string for the search.  
By default we will run the APP on the port 5000 on our localhost.  
The search will run on the twitter/twitter_data field news_text.

In case if you want to add any other method please feel free to modify the [source code](https://github.com/kurbakov/project_a/blob/master/api/scr/__init__.py) so you can add any other method that you consider important for your code.

