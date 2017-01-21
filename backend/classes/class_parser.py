# class to work with JSON
import json


class Parser:
    def __init__(self):
        print "Parser classes is used"

    @staticmethod
    def read_file(path):

        con = open(path, 'r')
        data = con.read()
        con.close()
        return data

    @staticmethod
    def parse_string(file_string):
        dictionary = json.loads(file_string)
        return dictionary

    @staticmethod
    def parse_twitter_data(twitter_out_data):
        res = list()

        for doc in twitter_out_data:
            my_dict = dict()

            json_str = json.dumps(doc._json)
            json_dict = json.loads(json_str)

            my_dict["news_id"] = json_dict.get("id")

            news_text = json_dict.get("text").encode('ascii', 'ignore').decode('ascii')
            http_start = news_text.find("http")
            if http_start > 0:
                news_text = news_text[:http_start-1]

            my_dict["news_text"] = news_text

            my_dict["news_created_at"] = json_dict.get("created_at")

            res.append(my_dict)

        return res
