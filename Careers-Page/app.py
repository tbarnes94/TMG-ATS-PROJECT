# Written by Thomas J Barnes
# Business Development Intern
# June 20, 2016
# 
# this flask framework connects the backend engine
# and front end html/css and javascript
from flask import Flask
from flask import request, render_template, jsonify, url_for
from jira import JIRA
import json, re, os
import python.auto_populate as auto_populate

# instantiates the Flask application
app = Flask(__name__)

# URL for the website
url = "http://0.0.0.0:5000"
# URL for creation of issues via JIRA REST API
# create_issue_url = "http://testjira.transmarketgroup.com:8080/rest/api/2/issue/"
jira_options = { 'server': 'http://64.94.36.24:8080/' }

jira = JIRA(options=jira_options, basic_auth=('tommy.barnes', 'password'))

global data

#####################
#    Constants      #
#####################

BLACKLIST = "Reject Blacklist"
WHITELIST = "Reject Whitelist"
MOVED_ON = "Moved On"
PHONE_SCREEN_REQUESTED = "Request Phone Screen"
INTERVIEW_ASSIGNED = "Assign Interview"
EXAM_ASSIGNED = "Assign Exam"
INTERVIEW_COMPLETE = "Interview Evaluation"
EXAM_COMPLETE = "Exam Completed"
OFFER_MADE = "Approve"


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
    #print "#################"
    #print "Web hook Received"
    #print "#################"
    data = request.get_json()
    
    issue = data['issue']
    '''
    print data
    print "**********************"

    How to get parent field from a sub-task
    print fields['parent']
    print fields['parent']['key']'''
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
            auto_populate.create_document("Testing.docx", {"EMPLOYEE" : "Daniel Smith"})
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
    # body = [{'Header':[{}],'Content':[]}]

    # # HEADER of multipart/form-data payload
    # # NOTE: Probably will not need Header information, but just in case...
    # hdr = sanitize(d[0:57])

    # # Indices where HEADER occurs
    # # Dispense the last one, as this is the end of the file
    # ind = [m.start()+57 for m in re.finditer(hdr,d)]
    # ind = ind[:len(ind)-1]

    # # Dictionary for storing Candidate profile information
    # # Store the header under the 'Header' namespace of 'body'
    # # Store the 'Content-Disposition'
    # my_dict = {}
    # body[0]['Header'][0]['Header'] = hdr
    # body[0]['Header'][0]['Content-Disposition'] = 'form-data'

    # # Looping through all occurrences of the HEADER
    # # NOTE: Many of these index offsets are hardcoded because their locations will not change, sorry for any confusion
    # for place, item in enumerate(ind):

    #     # Does not loop through on the last index to avoid IndexError
    #     if (place+1) < len(ind):
    #         # 'substring' is a portion of the data retrieved segmented by HEADER occurrences
    #         substring = d[ind[place]:ind[place+1]-56]

    #         # Does not run if 'name' is not found in substring (no desirable content)
    #         if d[ind[place]:ind[place+1]-56].find('name') != -1:

    #             # Index of where 'name' occurs in the substring
    #             nameIndex = substring.find('name')

    #             # Index of the closing quotation mark of an attribute (EX: name="Last"\r\nBarnes\r\n)
    #             #                                                                    ^
    #             quoteIndex = substring[nameIndex+6:].find('"') + (nameIndex+6) #double quotes

    #             # The attribute between the quotes will be the 'Key' when you store the profile content in the JSON object payload
    #             key = substring[nameIndex+6:quoteIndex]

    #             # Store content into JSON payload by dynamic key
    #             my_dict[key] = sanitize(substring[quoteIndex+2:len(substring)-1])

    # # Append content to the appropriate namespace
    # body[0]['Content'].append(my_dict)

    # # shorthanding to just the content part of the JSON object
    # content = body[0]['Content'][0]

    # JSON object corresponding to Candidate's issue fields
    # data = api_request % (content['First'],content['Last'],content['Email'],content['Phone'],content['Position'],content['PositionType'],content['Location'],content['School'],content['DegreeType']+' '+content['Degree'],content['Position']+\
    #     ' | '+content['PositionType']+' | '+content['Location']+' - '+content['Last']+','+content['First'])

    issue_dict={
            'project': { 'name': 'JIRA-ATS', 'key': 'ATS' },
            'issuetype': { 'name': 'Task' },
            'customfield_10783': '%s' % request.form['First'],
            'customfield_10784': '%s' % request.form['Last'],
            'customfield_10787': '%s' % request.form['Email'],
            'customfield_10792': '%s' % request.form['Phone'],
            'customfield_10790': '%s' % request.form['Position'],
            'customfield_10791': '%s' % request.form['PositionType'],
            'customfield_10794': '%s' % request.form['Location'],
            'customfield_10788': '%s' % request.form['School'],
            'customfield_10789': '%s' % request.form['DegreeType'] + ' ' + request.form['Degree'],
            'customfield_10909': '%s' % "daniel.smith",
            'customfield_10910': '%s' % "tommy.barnes",
            'customfield_10911': '%s' % "daniel.smith",
            'summary': '%s' % request.form['Position']+' | '+request.form['PositionType']+' | '+request.form['Location']+' - '+request.form['Last']+','+request.form['First'],
            'description': '[Write observations of the candidate here]'
            }
    # REST API using 'curl' and stores the output in r
    # r = subprocess.check_output(['curl','-D-','-u','tommy.barnes:password','-X','POST','--data',data,'-H','Content-Type: application/json',create_issue_url])
    new_issue = jira.create_issue(fields=issue_dict, prefetch=True)
    # issue key auto-generated by JIRA corresponding to Candidate
    # issue_key = json.loads(r.split()[-1])['key']

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

    # Assigning the 3 interviewers...

    #new_issue.update(fields = {"Assignee 1" : "daniel.smith", "Assignee 2" : "tommy.barnes", "Assignee 3" : "daniel.smith"})

    # Routes the Candidate to a page that thanks him/her for submitting
    return render_template('submitted.html')

if __name__ == "__main__":
    # initialize backend engine of the JIRA_Feeder Application
    app.run(host=url.split(':')[1][2:], port=int(url.split(':')[2]), debug=True)
