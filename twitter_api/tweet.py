import twitter
CONSUMER_KEY = 'iyijz0WauC47JhldDofD5Sxrq'
CONSUMER_SECRET ='FoHv0HGkYYrSgWcXEEdIXWyw8L3zCbQqXR69w2tZhLaW8qah52'
OAUTH_TOKEN = '2193588674-W5Zq9smc5F4RRVHI23E7AVFpgdLf9WcZQIKSJmA'
OAUTH_TOKEN_SECRET = 'Pr3CMTlToMrmPvnsReG5M06zDdtNtmiE8MaskOQpDhT34'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

print twitter_api


