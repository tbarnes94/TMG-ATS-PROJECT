import requests
from requests.auth import HTTPBasicAuth
import os, json

header = {"Content-Type" : "application/json", "Accept" : "application/json"}
url = "https://www.polleverywhere.com/multiple_choice_polls"

poll_json = '''{\
  	\"multiple_choice_poll\": {
  		\"id\":null,
  		\"updated_at\":null,
  		\"title\":\"Testing\!\",
  		\"opened_at\":null,
  		\"permalink\":null,
  		\"state\":\"opened\",
  		\"sms_enabled\":null,
  		\"twitter_enabled\":null,
  		\"web_enabled\":null,
  		\"sharing_enabled\":null,
  		\"simple_keywords\":null,
  		\"registered_participants_only\": true,
  		\"active\":true,
   		\"options\":[{
  			\"id\":null,
  			\"value\":\"red\",
  			\"keyword\":null
  		},{
  			\"id\":null,
  			\"value\":\"blue\",
  			\"keyword\":null
  		},{
  			\"id\":null,
  			\"value\":\"green\",
  			\"keyword\":null
  		}]
  	}
}'''

def create_poll():
	r = requests.post(url, data = poll_json, headers = header, auth=HTTPBasicAuth(os.environ["EMAIL"], os.environ["PSWD"]))
	print r.text
	print r
	return json.loads(r.text)

def start_poll(json_poll):
	r = requests.post(url, data = json_poll, headers = header, auth=HTTPBasicAuth(os.environ["EMAIL"], os.environ["PSWD"]))
	print r.text
	return json.loads(r.text)

poll = create_poll()
print poll
poll['multiple_choice_poll']['state'] = "opened"
poll = json.dumps(poll)
print poll
#print start_poll(poll)