from flask import Flask
from flask_restful import reqparse, Resource, Api
from flask_cors import CORS
import requests
import json

from . import config

app = Flask(__name__)
CORS(app)
api = Api(app)

parser = reqparse.RequestParser()


class Search(Resource):

    def get(self):

        parser.add_argument('q')
        query_string = parser.parse_args()

        url = config.es_twitter_index['twitter_data']+'/_search'
        query = {
            "query": {
                "multi_match": {
                    "fields": ["news_text"],
                    "query": query_string['q']
                }
            },
            "size": 100
        }

        resp = requests.post(url, data=json.dumps(query))
        data = resp.json()

        return data

api.add_resource(Search, config.api_base_url+'/search')
