# class to work with DB
# more info here:
#   - https://elasticsearch-py.readthedocs.io/en/master/
#   - http://elasticsearch-py.readthedocs.io/en/master/helpers.html#bulk-helpers

from elasticsearch import Elasticsearch


class Database:
    def __init__(self):
        self.es = Elasticsearch([{'host': '127.0.0.1', 'port': 443}])

    def create_index(self, index_name):
        self.es.indices.create(index=index_name, ignore=400)

    def delete_index(self, index_name):
        self.es.indices.delete(index=index_name, ignore=[400, 404])

    def insert_document(self, index_name, predefined_id, document):
        self.es.index(index=index_name, id=predefined_id, body=document, doc_type='tweet')

    def delete_document(self, index_name, predefined_id):
        self.es.delete(index=index_name, id=predefined_id, doc_type="tweet",)

    def select_all_documents(self, index_name):
        res = self.es.search(index=index_name, body={"query": {"match_all": {}}})
        return res

    def refresh_index(self, index_name):
        self.es.indices.refresh(index=index_name)

    def update_document(self, index_name, document_id, key, new_value):
        self.es.update(index=index_name, doc_type='tweet', id=document_id, body={"doc": {key: new_value}})

