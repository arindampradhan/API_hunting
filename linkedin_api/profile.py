from linkedin import linkedin

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
USER_TOKEN = ''
USER_SECRET = ''

RETURN_URL = '' #not require so much

auth = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY,CONSUMER_SECRET,USER_TOKEN,USER_SECRET,RETURN_URL,permissions=linkedin.PERMISSIONS.enums.values())



app = linkedin.LinkedInApplication(auth)

# work starts here
import json

connections = app.get_connections()


my_position = app.get_profile(selectors=['positions'])

print json.dumps(my_position,indent=2)

connection_id = connections['values'][0]['id']

connection_positions = app.get_profile(member_id = connection_id,selectors=['positions'])

print json.dumps(connection_positions,indent=2)
