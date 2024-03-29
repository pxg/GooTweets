import os
import sys
import tweepy

#USER_ID = 825324804  # DavouriteQ
USER_ID = 33557547  # Pete Goodman

# Default Values are for DavouriteQ posting
CONSUMER_KEY = os.getenv('GOO_CONSUMER_KEY', 'a9c5CRXeNeSqxHQJgYoSUg')
CONSUMER_SECRET = os.getenv('GOO_CONSUMER_SECRET',
                            'KPBNm41iLIqxC5pM1abvXqZzdt0qrpQfSkQYeGAS8')
ACCESS_TOKEN = os.getenv('GOO_ACCESS_TOKEN',
                         '825324804-bo1JevjUZUtstfXoKHyz8XirNIIBg9KFmPIlRKIt')
ACCESS_TOKEN_SECRET = os.getenv('GOO_ACCESS_TOKEN_SECRET',
                                '0R7DJq72qDLtMIkZ17xDIUUjyHMPef9KaNHu1zy3PJA')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Test tweet
# api = tweepy.API(auth)
# api.update_status('Hello World')
# sys.exit()


class CustomStreamListener(tweepy.StreamListener):
    auth = None

    def __init__(self, auth):
        super(CustomStreamListener, self).__init__()
        self.auth = auth

    def on_status(self, status):
        try:
            print "%s\t%s\t%s\t%s" % (status.text,
                                      status.author.screen_name,
                                      status.created_at,
                                      status.source,)
            # don't spam people
            tweet_text = status.text.replace('@', '_')
            api = tweepy.API(self.auth)
            api.update_status(tweet_text)

        except Exception, e:
            print >> sys.stderr, 'Encountered Exception:', e
            pass

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True

streaming_api = tweepy.streaming.Stream(auth, CustomStreamListener(auth), timeout=60)
streaming_api.filter(follow=[USER_ID])
#streaming_api.filter(follow=None, track=['bieber']) # Test search
