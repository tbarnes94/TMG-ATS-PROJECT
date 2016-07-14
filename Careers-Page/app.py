# Written by Thomas J Barnes
# Business Development Intern
# June 20, 2016
# 
# this flask framework connects the backend engine
# and front end html/css and javascript
from flask import Flask
from flask import request, render_template, jsonify, url_for
from jira import JIRA
import json, re, os, datetime, random
import python.auto_populate as auto_populate
import python.email_handler as email_handler

# instantiates the Flask application
app = Flask(__name__)

# URL for the website
url = "http://0.0.0.0:5000"
# URL for creation of issues via JIRA REST API
# create_issue_url = "http://testjira.transmarketgroup.com:8080/rest/api/2/issue/"
# jira_options = { 'server': 'http://testjira.transmarketgroup.com:8080/' }# LOCAL SERVER

jira_options = { 'server': 'http://64.94.36.24:8080/' }

jira = JIRA(options=jira_options, basic_auth=('tommy.barnes', 'password'))

global data

#####################
#    Constants      #
#####################

CURRENT_DATE = datetime.datetime.now().replace(hour=0,minute=0,second=0,microsecond=0)
BLACKLIST = "Reject Blacklist"
WHITELIST = "Reject Whitelist"
MOVED_ON = "Moved On"
PHONE_SCREEN_REQUESTED = "Request Phone Screen"
INTERVIEW_ASSIGNED = "Assign Interview"
EXAM_ASSIGNED = "Assign Exam"
INTERVIEW_COMPLETE = "Interview Evaluation"
EXAM_COMPLETE = "Exam Completed"
OFFER_MADE = "Approve"

custom_fields = {
    'FIRST'    : 'customfield_10783',
    'LAST'     : 'customfield_10784',
    'EMAIL'    : 'customfield_10787',
    'PHONE'    : 'customfield_10792',
    'POSITION' : 'customfield_10790',
    'TYPE'     : 'customfield_10791',
    'LOCATION' : 'customfield_10794',
    'DEGREE'   : 'customfield_10788',
    'TITLE'    : 'customfield_10789',
    'ASSIGNEE' : 'customfield_10909'
}

# Function that removes non-standard characters from profile information
def sanitize(string):
    return ''.join(c for c in string if c.isalnum() or \
        c == "_" or \
        c == "-" or \
        c == "@" or \
        c == "(" or \
        c == ")" or \
        c == "/" or \
        c == "." or \
        c == "+" or \
        c == " ")

def get_interviewer(my_list):
    num_interviewers = len(my_list)
    interviewer_index = random.randint(0,num_interviewers-1)
    return my_list[interviewer_index]

def lowerCase(letter):
    return chr(ord(letter)+32)

def reformat(attr, attr_type):
    if attr_type == 'DegreeType':
        return {'B.A': 'Undergraduate', 'B.S.': 'Undergraduate', 'M.A.': 'Graduate', 'M.S.': 'Graduate', 'PhD': 'Graduate'}[attr]
    elif attr_type == 'PositionType':
        return {'Internship': 'INTERN', 'Full Time': 'FULL TIME'}[attr]
    elif attr_type == "Phone":
        return '('+attr[:3]+') '+attr[3:6]+'-'+attr[6:]

# Function that handles HTTP GET requests (renders the Career page)
@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/test", methods=['GET'])
def test():
    return 'TESTING TEXT'

# Route for post request webhooks
@app.route('/webhooks', methods = ["POST"])
def webhooks():
    data = request.get_json()
    issue = data['issue']
    
    if 'transition' in data.keys():
        transition = data['transition']
        # stupid python with no switch cases

        # Handle various transitions however you want (Guaranteed to have to_status)
        if transition['transitionName'] == BLACKLIST:
            '''
            placeholders = {}
            placeholders["first"] = fields[FIRST]
            placeholders["last"] = fields[LAST]
            placeholders["email"] = "daniel.smith@aardv.com"
            placeholders["position"] = fields[POSITION]
            temp = "hi %s"
            email.send_email(placeholders, temp)'''
            print transition['transitionName']
        elif transition['transitionName'] == WHITELIST:
            print transition['transitionName']
        elif transition['transitionName'] == MOVED_ON:
            print transition['transitionName']
        elif transition['transitionName'] == PHONE_SCREEN_REQUESTED:
            print transition['transitionName']
        elif transition['transitionName'] == INTERVIEW_COMPLETE:
            print issue['fields']['parent'].keys()
            print transition['transitionName']
        elif transition['transitionName'] == EXAM_ASSIGNED:
            print transition['transitionName']
        elif transition['transitionName'] == EXAM_COMPLETE:
            print transition['transitionName']
        elif transition['transitionName'] == OFFER_MADE:
            fields = issue['fields']

            # Create dictionary for auto_populate as placeholders
            dic = { placeholder : fields[custom_fields[placeholder]] for placeholder in custom_fields }
            dic['EMPLOYEE'] = dic["FIRST"] + " " + dic["LAST"]

            # Create filled out document
            auto_populate.create_document("Testing", dic)

            # Send document to candidate
            email_handler.send_email(dic, email_handler.ACCEPT_MESSAGE, ["Testing_%s_%s"%(dic["FIRST"],dic["LAST"])])
            print transition['transitionName']
        elif transition['transitionName'] == "Create":
            print data['issue'].keys()
            print data['issue']['fields']['issue'].keys()
            print issue['fields']['parent'].keys()
            print data['transition']
        else:
            # Should not happen
            print "Transition not recognized: %s"%(transition['transitionName'])
            print issue['fields']
    else:
        print "No transition: "
        print data.keys()
        print data['issue'].keys()
        print issue['key']
    return "OK"

# Function that handles HTTP POST requests
@app.route("/data", methods=['POST'])
def post_data():
    # Retrieve data from Career website via HTTP POST request
    # 'body' list that will store the POST request's 'multipart/form-data' content
    d = request.get_data()

    try:
        with open('/home/tmgaws/TMG-ATS-PROJECT/Assignee-App/interviewers-%s.json'%CURRENT_DATE, 'rb') as fh:
            my_dict = json.load(fh)
    except IOError:
        with open('/home/tmgaws/TMG-ATS-PROJECT/Assignee-App/interviewers-backup.json', 'rb') as fh:
            my_dict = json.load(fh)

    ASSIGNEE_DISPLAY_NAME = get_interviewer(my_dict[0]["Locations"][request.form['Location']]["Degrees"][reformat(request.form['DegreeType'],'DegreeType')][reformat(request.form['PositionType'],'PositionType')]["Requisitions"][request.form['Position']]["Round 1"])
    ASSIGNEE_TUPLE = ASSIGNEE_DISPLAY_NAME.split(' ')
    ASSIGNEE = lowerCase(ASSIGNEE_TUPLE[0][0]) + ASSIGNEE_TUPLE[0][1:] + '.' + lowerCase(ASSIGNEE_TUPLE[1][0]) + ASSIGNEE_TUPLE[1][1:]

    issue_dict={
            'project': { 'name': 'JIRA-ATS', 'key': 'ATS' },
            'issuetype': { 'name': 'Task' },
            'customfield_10783': '%s' % request.form['First'],
            'customfield_10784': '%s' % request.form['Last'],
            'customfield_10787': '%s' % request.form['Email'],
            'customfield_10792': '%s' % reformat(request.form['Phone'],'Phone'),
            'customfield_10790': '%s' % request.form['Position'],
            'customfield_10791': '%s' % request.form['PositionType'],
            'customfield_10794': '%s' % request.form['Location'],
            'customfield_10788': '%s' % request.form['School'],
            'customfield_10789': '%s' % request.form['DegreeType'] + ' ' + request.form['Degree'],
            'customfield_10909': '%s' % ASSIGNEE,
            'summary': '%s' % request.form['Position']+' | '+request.form['PositionType']+' | '+request.form['Location']+' - '+request.form['Last']+','+request.form['First'],
            'description': '[Write observations of the candidate here]'
            }
    # REST API using 'curl' and stores the output in r
    # r = subprocess.check_output(['curl','-D-','-u','tommy.barnes:password','-X','POST','--data',data,'-H','Content-Type: application/json',create_issue_url])
    new_issue = jira.create_issue(fields=issue_dict, prefetch=True)

    # distinct file name for Candidate's resume
    resume_name = '%s-%s_(%s).pdf' % (request.form['First'], request.form['Last'], new_issue.key)

    # write resume PDF to server location
    with open (resume_name,'w') as fh:
        fh.write(d[d.find("%PDF"):len(d)-59])
    
    # 'attachment_url' is the URI of attaching files to specific issues in JIRA REST API
    # attachment_url = 'http://testjira.transmarketgroup.com:8080/rest/api/2/issue/%s/attachments' % issue_key
    
    # attach resume to issue corresponding to 'issue_key' and delete it locally
    jira.add_attachment(new_issue, resume_name)
    os.remove(resume_name)

    # Routes the Candidate to a page that thanks him/her for submitting
    return render_template('submitted.html')

if __name__ == "__main__":
    # initialize backend engine of the JIRA_Feeder Application
    app.run(host=url.split(':')[1][2:], port=int(url.split(':')[2]), debug=True)
