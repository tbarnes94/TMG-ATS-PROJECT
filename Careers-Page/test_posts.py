# sending simple post request to Jira

import requests
from requests.auth import HTTPBasicAuth

header = {"Content-Type" : "application/json"}
url = "http://testjira.transmarketgroup.com:8080/rest/api/2/issue/"

issue_dict='''{
	"fields" : {
	    "project": { "name": "JIRA-ATS", "key": "ATS" },
	    "issuetype": { "name": "Task" },
	    "customfield_10783": "Daniel",
	    "customfield_10784": "Smith",
	    "customfield_10787": "dnsmith@mit.edu",
	    "customfield_10792": "1111111212",
	    "customfield_10790": "Business Development",
	    "customfield_10791": "Intern",
	    "customfield_10794": "Chicago",
	    "customfield_10788": "MIT",
	    "customfield_10789": "CS BS",
	    "summary": "Business Development | Intern | Chicago | Daniel Smith",
	    "description": "[Write observations of the candidate here]"
    }
}'''

r = requests.post(url, data=str(issue_dict), headers=header, auth=HTTPBasicAuth("tommy.barnes", "password"))
print r.text