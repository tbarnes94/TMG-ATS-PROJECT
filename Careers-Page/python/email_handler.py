# Testing emails in python

import smtplib
import os, time

from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders


BLACKLIST_MESSAGE = '''From: From TMG Recruiting <%s>
To: To %s <%s>
Subject: Rejection Email

Hi %s,

Thank you for applying for the position of %s. However, blah blah blah...

Best,

TMG Recruiting
'''

ACCEPT_MESSAGE = '''

Hi {FIRST},

Thank you for applying for the position of {POSITION}. We would be delighted if you joined the team. Fill out these documents...

Best,

TMG Recruiting

'''

COMPLETED_PATH = "/home/tmgaws/TMG-ATS-PROJECT/documents/complete"

AARDV_EMAIL = os.getenv("EMAIL")
AARDV_PSWD = os.getenv("PSWD")


# Takes a recipient dictionary which contains all of relevant info of applicant
# (first name, last name, position they were applying to, email)
def send_email(recipient, template, attachments):
	# Connect to Gmail
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(AARDV_EMAIL, AARDV_PSWD)

	# Create email text by filling in placeholders
	msg_text = fill_placeholders(template, recipient)

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
		attachment.set_payload(open(os.path.join(COMPLETED_PATH, filename + ".docx"), "rb").read())
		Encoders.encode_base64(attachment)
		attachment.add_header('Content-Disposition', 'attachment; filename="%s.docx"'%(filename))
		msg.attach(attachment)

	# NEEDS TO BE CHANGED TO RECIPIENT EMAIL
	server.sendmail(AARDV_EMAIL, AARDV_EMAIL, msg.as_string())
	server.quit()
	
#send_email({"EMAIL" : "daniel.smith@aardv.com", "FIRST" :"Daniel", "POSITION" : "Trader"}, accept_message)

# Replaces placeholders in text with their value according to recirpient and sender dictionaries
# and returns new text
def fill_placeholders(text, recipient, sender = {}):
	for placeholder in recipient:
		text = text.replace("{%s}"%(placeholder), recipient[placeholder])
	for placeholder in sender:
		text = text.replace("{%s}"%(placeholder), sender[placeholder])
	return text
