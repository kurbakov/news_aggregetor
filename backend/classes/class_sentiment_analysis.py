# file to compute sentiment value of the string
# http://nltk-trainer.readthedocs.io/en/latest/
# https://pythonprogramming.net/sentiment-analysis-module-nltk-tutorial/
# https://pypi.python.org/pypi/textblob
# http://andybromberg.com/sentiment-analysis-python/
# http://text-processing.com/docs/sentiment.html
# http://www.nltk.org/howto/sentiment.html

import json
import nltk
from nltk.probability import FreqDist
import pickle


class SentimentAnalysis:
    def __init__(self, pos, neg, classifier):
        self.positive_path = pos
        self.negative_path = neg
        self.classifier_path = classifier

    def get_positive_sample(self):
        f = open(self.positive_path)

        res = []
        for tweet in f:
            json_parsed = json.loads(tweet)
            res.append((json_parsed["text"], "positive"))

        f.close()
        return res

    def get_negative_sample(self):
        f = open(self.negative_path)

        res = []
        for tweet in f:
            json_parsed = json.loads(tweet)
            res.append((json_parsed["text"], "negative"))

        f.close()
        return res

    @staticmethod
    def get_words_in_tweets(tweets):
        all_words = []
        for (words, sentiment) in tweets:
            all_words.extend(words)
        return all_words

    def get_word_features(self, wordlist):
        nltk_wordlist = FreqDist(wordlist)
        self.word_features = nltk_wordlist.keys()

    def extract_features(self, document):
        document_words = set(document)
        features = {}
        for word in self.word_features:
            features['contains(%s)' % word] = (word in document_words)
        return features

    def save_classifier(self, classifier):
        f = open(self.classifier_path, 'wb')
        pickle.dump(classifier, f, -1)
        f.close()

    def learn_classifier(self):
        print 'get positive twitter data...'
        pos_tweets = self.get_positive_sample()
        print 'get negative twitter data...'
        neg_tweets = self.get_negative_sample()

        print 'build full data set'
        tweets = []
        for (words, sentiment) in pos_tweets + neg_tweets:
            words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
            tweets.append((words_filtered, sentiment))

        print 'get word features...'
        self.get_word_features(self.get_words_in_tweets(tweets))

        print 'create training set...'
        training_set = nltk.apply_features(self.extract_features, tweets)

        print 'learn classifier...'
        classifier = nltk.classify.NaiveBayesClassifier.train(training_set)

        print 'save classifier...'
        self.save_classifier(classifier)

    def load_classifier(self):
        pos_tweets = self.get_positive_sample()
        neg_tweets = self.get_negative_sample()

        tweets = []
        for (words, sentiment) in pos_tweets + neg_tweets:
            words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
            tweets.append((words_filtered, sentiment))

        self.get_word_features(self.get_words_in_tweets(tweets))

        f = open(self.classifier_path, 'rb')
        classifier = pickle.load(f)
        f.close()
        return classifier

    def compute_sentiment_value(self, classifier, string):
        neg_prob = classifier.prob_classify(self.extract_features(string.split())).prob('negative')
        res = dict()
        res["negative_probability"] = neg_prob
        res["positive_probability"] = 1-neg_prob
        return res


# if __name__ == '__main__':
#
#     POSITIVE = "/Users/dmytrokurbakov/Desktop/news/be/sa/negative_tweets.json"
#     NEGATIVE = "/Users/dmytrokurbakov/Desktop/news/be/sa/positive_tweets.json"
#     CLASSIFIER_PATH = "/Users/dmytrokurbakov/Desktop/news/be/sa/classifier.pickle"
#
#     sa = Sentiment_analysis(POSITIVE, NEGATIVE, CLASSIFIER_PATH)
#     # sa.learn_classifier()
#     classifier = sa.load_classifier()
#     my_data = "my twitt is here!"
#     result = sa.compute_sentiment_value(classifier, my_data)
#     print result
