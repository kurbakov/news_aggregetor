from elasticsearch import Elasticsearch
import json

path_to_data_sample = "/Users/dmytrokurbakov/Desktop/my_git/project_a/temp/data_sample.json"

def read_file(path):
    con = open(path, 'r')
    data = con.read()
    con.close()
    return data

es = Elasticsearch()
es.indices.create(index="twitter_data", ignore=400)

data_string = read_file(path_to_data_sample)
data_dict = json.loads(data_string)

for element in data_dict:
    es.index(index="twitter_data", id=element.get("id"), body=element, doc_type='tweet')

es.indices.refresh(index="twitter_data")

res = es.search(index="twitter_data", body={"query": {"match_all": {}}})
print res

es.indices.delete(index="twitter_data", ignore=[400, 404])
