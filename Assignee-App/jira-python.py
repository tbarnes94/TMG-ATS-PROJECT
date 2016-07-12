from jira import JIRA
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('myKeyfile.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("Prototyping Interview Database").sheet1

ROWS = 500
COLS = 4

def main():
	for i in range(1,ROWS*COLS+1):
		if wks.cell(i%ROWS,i%COLS).value != "":
			print wks.cell(i%ROWS,i%COLS).value
			# print wks.cell(i+1,6).value
			# print wks.cell(i+1,7).value
			raw_input()


# jira_options = { 'server': 'http://testjira.transmarketgroup.com:8080/' }

# jira = JIRA(options=jira_options, basic_auth=('tommy.barnes', 'password'))

# issue = jira.issue('ATS-48')

# Template for the JSON object that becomes the issue fields:
    # First Name
    # Last Name
    # Email Address
    # Phone Number
    # Position
    # Position Type
    # Location
    # Degree Type + Degree
    # Issue Title ('Position | Position Type | Location - Last, First')

# issue_dict={
# 			'project': { 'name': 'JIRA-ATS', 'key': 'ATS' },
# 			'issuetype': { 'name': 'Task' },
# 			'customfield_10783': '%s',
# 			'customfield_10784': '%s',
# 			'customfield_10787': '%s',
# 			'customfield_10792': '%s',
# 			'customfield_10790': '%s',
# 			'customfield_10791': '%s',
# 			'customfield_10794': '%s',
# 			'customfield_10788': '%s',
# 			'customfield_10789': '%s',
# 			'summary': '%s',
# 			'description': '[Write observations of the candidate here]'
# 			}
# new_issue = jira.create_issue(fields=issue_dict, prefetch=True)
# issue.update( assignee={ 'name': 'daniel.smith' } )
# jira.assign_issue(issue,'tommy.barnes')
# resume_name = '/home/tommy.barnes/Downloads/Thomas Barnes - Resume.pdf'
# with open (resume_name,'rb') as fh:
# 	jira.add_attachment(new_issue, fh)
# 	
# print jira.search_issues(jql_str="project=\"JIRA-ATS\" AND issueKey=\"ATS-30\"",
# 						startAt=0, maxResults=50, validate_query=True, fields='assignee',
# 						expand=None, json_result=True)
# print jira.search_assignable_users_for_issues(username='', project='JIRA-ATS', issueKey='ATS-30',
# 										expand=None, startAt=0, maxResults=50)
if __name__ == '__main__':
	main()