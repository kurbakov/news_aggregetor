# need to rewrite from scratch

# libraries
import json
import os

# my classes
from classes.class_parser import Parser
from classes.class_twitter import Twitter
from classes.class_database import Database
from classes.class_sentiment_analysis import SentimentAnalysis

# Global variables

CREDENTIALS_FILE = "../../credentials.json"
CONFIG_FILE = "data/twitter_accounts.json"
POSITIVE = "data/negative_tweets.json"
NEGATIVE = "data/positive_tweets.json"
CLASSIFIER_PATH = "sentiment_analysis/classifier.pickle"

if __name__ == '__main__':
    p = Parser()
    credentials_string = p.read_file(CREDENTIALS_FILE)
    credentials_dict = p.parse_string(credentials_string)

    TWITTER_CKEY = credentials_dict.get("twitter_ckey")
    TWITTER_ATOCKEN = credentials_dict.get("twitter_tocken")
    TWITTER_CSECRET = credentials_dict.get("twitter_csecret")
    TWITTER_ATOCKEN_SECRET = credentials_dict.get("twitter_tocken_secret")

    twitter_api = Twitter(TWITTER_CKEY, TWITTER_CSECRET, TWITTER_ATOCKEN, TWITTER_ATOCKEN_SECRET)

    sa = SentimentAnalysis(POSITIVE, NEGATIVE, CLASSIFIER_PATH)
    classifier = sa.load_classifier()

    # get data from Elasticsearch!!!!!!
    # twitter_accounts = p.read_file(CONFIG_FILE)
    # twitter_accounts = p.parse_string(twitter_accounts)

    final_list = list()
    for account in twitter_accounts:

        twitter_out_data = twitter_api.get_twitts(twitter_id=account.get("id"), last_twitter_id=account.get("max_twitter_id"))
        parsed_twitter_data = p.parse_twitter_data(twitter_out_data)

#         for news in parsed_twitter_data:

#             res = dict()

#             res["id"] = news.get("news_id")
#             res["news_created_at"] = news.get("news_created_at")
#             res["news_text"] = news.get("news_text")
#             res["twitter_name"] = account.get("twitter_name")
#             res["twitter_tag"] = account.get("twitter_tag")
#             res["twitter_page"] = account.get("twitter_page")
#             res["country"] = account.get("country")
#             res["city"] = account.get("city")
#             res["longitude"] = account.get("longitude")
#             res["latitude"] = account.get("latitude")
#             res["language"] = account.get("language")

#             sa_results = sa.compute_sentiment_value(classifier, news.get("news_text"))

#             res["positive_probability"] = sa_results.get("positive_probability")
#             res["negative_probability"] = sa_results.get("negative_probability")

#             final_list.append(res)

#     # clean the file
#     open('/Users/dmytrokurbakov/Desktop/data_sample.json', 'w').close()

#     # write data
#     with open('/Users/dmytrokurbakov/Desktop/data_sample.json', 'w') as fout:
#         json.dump(final_list, fout)

#     # for el in parsed_twitter_data:
#     #     if el.get("news_id") > TWITT_LAST_ID:
#     #         TWITT_LAST_ID = el.get("news_id")
#     #
#     # print parsed_twitter_data
