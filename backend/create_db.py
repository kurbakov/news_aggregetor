'''
this file is to deploy the data base so to be sure
we use all the same data base in the backend wuth the same setup.
'''

# dependencies
from database import Database

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

    es.delete_index("twitter")
    es.delete_index("user")
