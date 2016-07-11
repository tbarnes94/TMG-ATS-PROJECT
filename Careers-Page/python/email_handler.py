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

accept_message = '''

Hi %s,

Thank you for applying for the position of %s. We would be delighted if you joined the team. Fill out these documents...

Best,

TMG Recruiting

'''

template_path = "/home/tmgaws/TMG-ATS-PROJECT/documents/complete"

AARDV_EMAIL = os.getenv("EMAIL")
AARDV_PSWD = os.getenv("PSWD")


# Takes a recipient dictionary which contains all of relevant info of applicant
# (first name, last name, position they were applying to, email)
def send_email(recipient, template, attachments):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(AARDV_EMAIL, AARDV_PSWD)

	msg_text = template%(recipient["FIRST"], recipient["POSITION"])

	# Create message and attach body
	msg = MIMEMultipart()
	body = MIMEMultipart('alternative')
	body.attach(MIMEText(msg_text))
	msg.attach(body)

	# Set headers TEMPORARY
	msg['Subject'] = "TMG Application Status"
	msg['From'] = AARDV_EMAIL
	msg['To'] = recipient["FIRST"] + recipient["LAST"]

	# Add attachment
	for filename in attachments:
		attachment = MIMEBase('application', "octet-stream")
		attachment.set_payload(open(os.path.join(template_path, filename + ".docx"), "rb").read())
		Encoders.encode_base64(attachment)
		attachment.add_header('Content-Disposition', 'attachment; filename="%s.docx"'%(filename))
		msg.attach(attachment)

	server.sendmail(AARDV_EMAIL, recipient['EMAIL'], msg.as_string())
	server.quit()
	print "Email sent!"
	
#send_email({"EMAIL" : "daniel.smith@aardv.com", "FIRST" :"Daniel", "POSITION" : "Trader"}, accept_message)
