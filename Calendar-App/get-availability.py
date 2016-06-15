from __future__ import print_function
import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

import datetime, calendar

import json, simplejson

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# x=[
#     {
#         "Interview Groups":
#             {
#                 "150":
#                     {
#                         "Round1": "tommy.barnes", 
#                         "Round2": "darren.street", 
#                         "Round3": "jon.watson"
#                     }
#             },
#         "Availability": 
#             None
#     }
# ]

# with open ('calendar_repo.json','w') as f:
#     f.write(json.dumps(x,indent=4,sort_keys=True,separators=(",",": ")))
global calendar_repo
with open ('candidate_repo.json','r') as f:
    calendar_repo = json.load(f)
# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'

# def sanitize(string):
#     return ''.join(c for c in string if c.isalnum() or \
#         c == "_" or \
#         c == "-" or \
#         c == "@" or \
#         c == "(" or \
#         c == ")" or \
#         c == "/" or \
#         c == "." or \
#         c == "+")

timeslotCounter = 0

def weekday(date_string):
    (year,month,day) = [int(c) for c in str(date_string).split('T')[0].split('-')]
    return {0: 'Monday',
            1: 'Tuesday',
            2: 'Wednesday',
            3: 'Thursday',
            4: 'Friday',
            5: 'Saturday',
            6: 'Sunday'}[calendar.weekday(year,month,day)]

def findNextFriday(date_string):
    date = datetime.datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S')
    fridayCount = 0
    while fridayCount < 2:
        date = date + datetime.timedelta(days=1)
        if weekday(str(date)[:10]+'T') == 'Friday':
            fridayCount += 1
    return str(date).split(' ')[0]+'T17:00:00-05:00'

def interviewSlots(start, end, creator, event_summary):
    date = datetime.datetime.strptime(start[:-6], '%Y-%m-%dT%H:%M:%S')
    end = datetime.datetime.strptime(end[:-6], '%Y-%m-%dT%H:%M:%S')
    now_date = start.split('T')[0]
    next_date = date + datetime.timedelta(hours=1)
    earliest = datetime.datetime.strptime(now_date+'T08:00:00', '%Y-%m-%dT%H:%M:%S')
    latest = datetime.datetime.strptime(now_date+'T17:00:00', '%Y-%m-%dT%H:%M:%S')
    print('e-- ',earliest,'l--',latest, date, next_date, end)
    # global timeslotCounter
    first = creator.split('.')[0]
    first = chr(ord(first[0]) - 32) + first[1:]
    last = creator.split('.')[1]
    last = chr(ord(last[0]) - 32) + last[1:]
    print(first,last)
    while next_date < end:
        # print('"e--', earliest, '"d--',  date, '"nd--', next_date, '"end--', end, '"l--', latest,'"', date >= earliest,date < latest)
        if date >= earliest and date < latest:
            print("Adding availability for %s %s"%(first,last), "DATE: "+str(date).split(' ')[0]+" TIME: "+str(date).split(' ')[1]+"-"+str(next_date).split(' ')[1])
            #TODO store availability for each interviewer
            user = "%s.%s" % (first,last)
            my_dict =   {  
                            event_summary: {
                                'start': str(date), 
                                'end': str(next_date) 
                            } 
                        }
            print('MY_DICT',my_dict)
            try:
                calendar_repo[0]['Availability'][0][user].append(my_dict) 
            except:
                calendar_repo[0]['Availability'][0][user] = []
                calendar_repo[0]['Availability'][0][user].append(my_dict)
            raw_input('1')
        date = next_date
        next_date = date + datetime.timedelta(hours=1)
    if next_date - end != datetime.timedelta(0) and date >= earliest and date < latest:
        if next_date <= latest:
            print("Adding availability for %s %s"%(first,last), "DATE: "+str(end).split(' ')[0]+" TIME: "+str(end).split(' ')[1]+"-"+str(next_date).split(' ')[1])
            #TODO store availability for each interviewer
            #
            user = "%s.%s" % (first,last)
            my_dict =   {  
                            event_summary: {
                                'start': str(end), 
                                'end': str(next_date) 
                            } 
                        }
            print('MY_DICT',my_dict)
            try:
                calendar_repo[0]['Availability'][0][user].append(my_dict) 
            except:
                calendar_repo[0]['Availability'][0][user] = []
                calendar_repo[0]['Availability'][0][user].append(my_dict)
            raw_input('2')
        else:
            print("Adding availability for %s %s"%(first,last), "DATE: "+str(end).split(' ')[0]+" TIME: "+str(end).split(' ')[1]+"-"+str(latest).split(' ')[1])
            #TODO store availability for each interviewer
            #
            user = "%s.%s" % (first,last)
            my_dict =   {  
                            event_summary: {
                                'start': str(date), 
                                'end': str(latest) 
                            } 
                        }
            print('MY_DICT',my_dict)
            try:
                calendar_repo[0]['Availability'][0][user].append(my_dict) 
            except:
                calendar_repo[0]['Availability'][0][user] = []
                calendar_repo[0]['Availability'][0][user].append(my_dict)
            raw_input('3')
    elif next_date <= latest and date >= earliest and date < latest:
        print("Adding availability for %s %s"%(first,last), "DATE: "+str(date).split(' ')[0]+" TIME: "+str(date).split(' ')[1]+"-"+str(end).split(' ')[1])
        #TODO store availability for each interviewer
        #
        user = "%s.%s" % (first,last)
        my_dict =   {  
                        event_summary: {
                            'start': str(date), 
                            'end': str(end) 
                        } 
                    }
        print('MY_DICT',my_dict)
        try:
            calendar_repo[0]['Availability'][0][user].append(my_dict) 
        except:
            calendar_repo[0]['Availability'][0][user] = []
            calendar_repo[0]['Availability'][0][user].append(my_dict)
        raw_input('4')
    elif date >= earliest and date < latest:
        print("Adding availability for %s %s"%(first,last), "DATE: "+str(date).split(' ')[0]+" TIME: "+str(date).split(' ')[1]+"-"+str(end).split(' ')[1])
        #TODO store availability for each interviewer
        #
        user = "%s.%s" % (first,last)
        my_dict =   {  
                        event_summary: {
                            'start': str(date), 
                            'end': str(latest) 
                        } 
                    }
        print('MY_DICT',my_dict)
        try:
            calendar_repo[0]['Availability'][0][user].append(my_dict) 
        except:
            calendar_repo[0]['Availability'][0][user] = []
            calendar_repo[0]['Availability'][0][user].append(my_dict)
        raw_input('5')
    with open('candidate_repo.json','w') as fh:
        fh.write(json.dumps(calendar_repo, indent=4, separators=(",",": ")))

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    nextFriday = findNextFriday(now[:-8])
    print('It is now '+now)
    print('Getting all upcoming events on the Events List')
    eventsResult = service.events().list(
        calendarId='%s@aardv.com'%calendar_repo[0]['Interview Groups'][0]['150']['Round1'], 
        timeMin=now, 
        timeMax=nextFriday,
        singleEvents=True, 
        orderBy='startTime').execute()
    # 'aardv.com_87kc5qltg7ec390cn449ck4eps@group.calendar.google.com'
    events = eventsResult.get('items', [])
    if not events:
        print('No upcoming events found.')
    global candidate_repo
    for num, event in enumerate(events):
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event['end'].get('dateTime', event['end'].get('date'))
        start_date = start.split('T')[0]
        start_time = start.split('T')[1].split('-')[0]
        time_zone = start.split('T')[1][-6:]
        end_date = end.split('T')[0]
        end_time = end.split('T')[1].split('-')[0]
        try:
            event_summary = event['summary']
        except:
            event_summary = "busy"
        # print(str(num+1)+'.\t', 
        #     event_summary+'\n\t', 
        #     start_date+'\t', 
        #     start_time+'-'+end_time+'\t', 'Time Zone: '+time_zone+'\t', 
        #     weekday(start), 
        #     nextFriday)
        if '[Interview Slot]' in event_summary:
            # print(event)
            print('\n'+event_summary)
            creator = event['creator']['email'].split('@')[0]
            # print('AVAILABLE FROM %s to %s on %s' % (start_time,end_time,start_date))
            interviewSlots(start,end,creator,event_summary)


if __name__ == '__main__':
    main()
