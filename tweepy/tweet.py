#!/usr/bin/env python

import tweepy

CONSUMER_KEY = "iyijz0WauC47JhldDofD5Sxrq"
CONSUMER_SECRET = "FoHv0HGkYYrSgWcXEEdIXWyw8L3zCbQqXR69w2tZhLaW8qah52"


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.secure = True
auth_url = auth.get_authorization_url()
print 'Please authorize: ' + auth_url
verifier = raw_input('PIN: ').strip()
auth.get_access_token(verifier)
print "ACCESS_KEY = '%s'" % auth.access_token.key
print "ACCESS_SECRET = '%s'" % auth.access_token.secret

