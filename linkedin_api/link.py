from linkedin import linkedin

CONSUMER_KEY = '75m67zxcei46ns'
CONSUMER_SECRET = 'ZBSPI4EgOBAbIfUQ'
USER_TOKEN = 'd797ddd3-8a54-4db3-b026-d6e3eb7b18f2'
USER_SECRET = '93a4a6a1-9a7e-4d69-9897-bfacbc6a0123'

RETURN_URL = '' #not require so much

auth = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY,CONSUMER_SECRET,USER_TOKEN,USER_SECRET,RETURN_URL,permissions=linkedin.PERMISSIONS.enums.values())



app = linkedin.LinkedInApplication(auth)
print app.get_profile()

# import json
# print json.dumps(app.get_profile(),indent=2)
