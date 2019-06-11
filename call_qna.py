import http.client, urllib.parse, time, sys
import json
from json import decoder
import secret_keys.config as config

#.config.py
#from secret_keys import config
# Represents the various elements used to create HTTP request URIs
# for QnA Maker operations.
# From Publish Page
# Example: YOUR-RESOURCE-NAME.azurewebsites.net
# CAUTION: This is not the exact value of HOST field
# HOST trimmed to work with http library
host = config.HOST

# Authorization endpoint key
# From Publish Page
endpoint_key = config.ENDPOINT_KEY

# Management APIs postpend the version to the route
# From Publish Page
# Example: /knowledgebases/ZZZ15f8c-d01b-4698-a2de-85b0dbf3358c/generateAnswer
# CAUTION: This is not the exact value after POST
# Part of HOST is prepended to route to work with http library
route = config.ROUTE

# JSON format for passing question to service
#question = "{'question': 'How can I cancel my hotel reservation?','top': 3}";
question = "{'question': 'How can I cancel my hotel reservation?'}";

# Add post request
headers = {
    'Authorization': 'EndpointKey ' + endpoint_key,
    'Content-Type': 'application/json'
  }

try:
  conn = http.client.HTTPSConnection(host,port=443)

  conn.request ("POST", route,  question, headers)

  response = conn.getresponse ()
  #print ("Response {}".format(response))
  answer = response.read ()
  #print ("answer {}".format(answer))
  #answer = json.loads(response.decode("utf-8"))
  print(json.dumps(json.loads(answer), indent=4))

except :
    print ("Unexpected error:", sys.exc_info()[0])
    print ("Unexpected error:", sys.exc_info()[1])