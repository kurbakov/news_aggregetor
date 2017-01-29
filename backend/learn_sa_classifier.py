# Global dependencies
import os

# Local dependencies
from classes.class_sentiment_analysis import SentimentAnalysis

#####################################################
# Global variables
#####################################################


working_directory = os.path.dirname(__file__)
POSITIVE = working_directory+"/data/negative_tweets.json"
NEGATIVE = working_directory+"/data/positive_tweets.json"
CLASSIFIER_PATH = working_directory+"/sentiment_analysis/classifier.pickle"

#####################################################
# Main function
#####################################################


if __name__ == '__main__':
    if os.path.exists(CLASSIFIER_PATH):
        os.remove(CLASSIFIER_PATH)

    sa = SentimentAnalysis(POSITIVE, NEGATIVE, CLASSIFIER_PATH)
    sa.learn_classifier()

    # test that classifier works:

    # load classifier
    classifier = sa.load_classifier()

    # check if it works
    my_data = "my twitt is here!"
    result = sa.compute_sentiment_value(classifier, my_data)
    print result
