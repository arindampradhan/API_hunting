from linkedin import linkedin

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
USER_TOKEN = ''
USER_SECRET = ''

RETURN_URL = '' #not require so much

auth = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY,CONSUMER_SECRET,USER_TOKEN,USER_SECRET,RETURN_URL,permissions=linkedin.PERMISSIONS.enums.values())



app = linkedin.LinkedInApplication(auth)
print app.get_profile()

# import json
# print json.dumps(app.get_profile(),indent=2)
