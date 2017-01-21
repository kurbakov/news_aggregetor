# class to work with DB
# more info here:
#   - https://elasticsearch-py.readthedocs.io/en/master/
#   - http://elasticsearch-py.readthedocs.io/en/master/helpers.html#bulk-helpers

from elasticsearch import Elasticsearch


class Database:
    def __init__(self):
        self.es = Elasticsearch([{'host': '127.0.0.1', 'port': 9200}])

    def create_index(self, index_name, mapping):
        self.es.indices.create(index=index_name, body=mapping, ignore=400)

    def delete_index(self, index_name):
        self.es.indices.delete(index=index_name, ignore=[400, 404])

    def insert_document(self, index_name, document, predefined_id, data):
        self.es.index(index=index_name, id=predefined_id, body=data, doc_type=document)

    def delete_document(self, index_name, document, predefined_id):
        self.es.delete(index=index_name, doc_type=document, id=predefined_id)

    def refresh_index(self, index_name):
        self.es.indices.refresh(index=index_name)


