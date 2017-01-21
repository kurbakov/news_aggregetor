# http://adilmoujahid.com/posts/2014/07/twitter-analytics/
# http://docs.tweepy.org/en/v3.5.0/api.html

# class to work with twitter
import tweepy


class Twitter:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        print "constructor for Twitter class!"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    # https://dev.twitter.com/rest/reference/get/statuses/user_timeline
    def get_twitts(self, twitter_id, last_twitter_id):
        return self.api.user_timeline(
            user_id=twitter_id,
            since_id=last_twitter_id,
            include_rts=False,
            contributor_details=False,
            exclude_replies=True,
            trim_user=False,
            count=300)
