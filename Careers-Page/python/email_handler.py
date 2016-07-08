# Testing emails in python

import smtplib
import os, time

from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders


blacklist_message = '''From: From TMG Recruiting <%s>
To: To %s <%s>
Subject: Rejection Email

Hi %s,

Thank you for applying for the position of %s. However, blah blah blah...

Best,

TMG Recruiting
'''

accept_message = '''From: From TMG Recruiting <%s>
To: To %s <%s>
Subject: Accept Email

Hi %s,

Thank you for applying for the position of %s. We would be delighted if you could join the team. Fill out these documents...
Best,

TMG Recruiting

'''

template_path = "/home/tmgaws/TMG-ATS-PROJECT/documents/complete/Testing_Daniel_Smith.docx"

aardv_email = os.getenv("EMAIL")
aardv_pswd = os.getenv("PSWD")


# Takes a recipient dictionary which contains all of relevant info of applicant
# (first name, last name, position they were applying to, email)
def send_email(recipient, template):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(aardv_email, aardv_pswd)

	msg_text = template%(aardv_email, recipient["FIRST"], recipient["EMAIL"], recipient["FIRST"], recipient["POSITION"])

	# Create message and attach body
	msg = MIMEMultipart()
	body = MIMEMultipart('alternative')
	body.attach(MIMEText(msg_text))
	msg.attach(body)

	attachment = MIMEBase('application', "octet-stream")
	attachment.set_payload(open(template_path, "rb").read())
	Encoders.encode_base64(attachment)
	attachment.add_header('Content-Disposition', 'attachment; filename="Employee Agreement.docx"')
	msg.attach(attachment)

	server.sendmail(aardv_email, recipient['EMAIL'], msg.as_string())
	server.quit()
	print "Email sent!"
	
#send_email({"EMAIL" : "daniel.smith@aardv.com", "FIRST" :"Daniel", "POSITION" : "Trader"}, accept_message)
