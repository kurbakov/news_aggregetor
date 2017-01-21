'''
this file is to deploy the data base so to be sure
we use all the same data base in the backend with the same setup.
'''

# global dependencies
import json

# local dependencies
from classes.class_database import Database

# global variable
working_directory = "/Users/dmytrokurbakov/Desktop/my_git/project_a/"


def read_file(path):
    con = open(path, 'r')
    data = con.read()
    con.close()
    return data

if __name__ == '__main__':
    es = Database()

    twitter_settings = {
        "mappings:": {
            "twitter_account": {
                "properties": {
                    "id": {"type": "long"},
                    "twitter_name": {"type": "string"},
                    "twitter_tag": {"type": "string"},
                    "twitter_page": {"type": "string"},
                    "country": {"type": "string"},
                    "city": {"type": "string"},
                    "longitude": {"type": "double"},
                    "latitude": {"type": "double"},
                    "language": {"type": "string"},
                    "max_twitter_id": {"type": "long"},
                }
            },
            "twitter_data": {
                "properties": {
                    "id": {"type": "long"},
                    "news_text": {"type": "string"},
                    "twitter_page": {"type": "string"},
                    "twitter_tag": {"type": "string"},
                    "twitter_name": {"type": "string"},
                    "news_created_at": {"type": "date"},
                    "latitude": {"type": "double"},
                    "longitude": {"type": "double"},
                    "positive_probability": {"type": "double"},
                    "negative_probability": {"type": "double"}
                }
            }
        }
    }
    es.create_index("twitter", twitter_settings)

    user_settings = {
        "mappings": {
            "user_information": {
                "properties": {
                    "id": {"type": "long"},
                    "user_name": {"type": "string"},
                    "user_email": {"type": "string"},
                    "user_login": {"type": "string"},
                    "user_password": {"type": "string"}
                }
            }
        }
    }
    es.create_index("user", user_settings)

    # load twitter sample data
    twitter_data_str = read_file(working_directory+"backend/data/twitter_data_sample.json")
    twitter_data_list = json.loads(twitter_data_str)

    # push data to the database
    for element in twitter_data_list:
        es.insert_document(index_name="twitter", document='twitter_data', predefined_id=element.get("id"), data=element)

    # free memory
    twitter_data_str.strip()
    del twitter_data_list[:]

    # load twitter account data sample
    twitter_account_str = read_file(working_directory+"backend/data/twitter_accounts.json")
    twitter_account_list = json.loads(twitter_account_str)

    # push data to the database
    for element in twitter_account_list:
        es.insert_document(index_name="twitter", document='twitter_account', predefined_id=element.get("id"), data=element)

    # free memory
    twitter_account_str.strip()
    del twitter_account_list[:]

    # refresh the database
    es.refresh_index("twitter")

    es.delete_index("twitter")
    es.delete_index("user")
