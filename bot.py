import sys
import tweepy

# TODO: get new token here
USER_ID = 825324804
CONSUMER_KEY = 'a9c5CRXeNeSqxHQJgYoSUg'
CONSUMER_SECRET = 'KPBNm41iLIqxC5pM1abvXqZzdt0qrpQfSkQYeGAS8'
ACCESS_TOKEN = '825324804-bo1JevjUZUtstfXoKHyz8XirNIIBg9KFmPIlRKIt'
ACCESS_TOKEN_SECRET = '0R7DJq72qDLtMIkZ17xDIUUjyHMPef9KaNHu1zy3PJA'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        try:
            print "%s\t%s\t%s\t%s" % (status.text,
                                      status.author.screen_name,
                                      status.created_at,
                                      status.source,)
            # TODO: post the tweet
        except Exception, e:
            print >> sys.stderr, 'Encountered Exception:', e
            pass

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True

streaming_api = tweepy.streaming.Stream(auth, CustomStreamListener(), timeout=60)
#print >> sys.stderr, 'Filtering the public timeline for "%s"' % (' '.join(sys.argv[1:]),)
streaming_api.filter(follow=[USER_ID])