#!/usr/bin/env python

import sys
import tweepy

CONSUMER_KEY = 'iyijz0WauC47JhldDofD5Sxrq'
CONSUMER_SECRET = 'FoHv0HGkYYrSgWcXEEdIXWyw8L3zCbQqXR69w2tZhLaW8qah52'
ACCESS_KEY = '2193588674-W5Zq9smc5F4RRVHI23E7AVFpgdLf9WcZQIKSJmA'
ACCESS_SECRET = 'Pr3CMTlToMrmPvnsReG5M06zDdtNtmiE8MaskOQpDhT34'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.secure = True
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
api.update_status(sys.argv[1])


