from __future__ import print_function
import httplib2
import os, datetime

from apiclient import discovery
import oauth2client, json
from oauth2client import client
from oauth2client import tools

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_id.json'
APPLICATION_NAME = 'Interview DB - Google Sheet to JSON'

CURRENT_DAY = None
# NEXT_DAY = datetime.datetime.now() + datetime.timedelta(minutes=1)
NEXT_DAY = datetime.datetime.now() + datetime.timedelta(days=1)
# NEXT_DAY = NEXT_DAY.replace(second=0, microsecond=0)
NEXT_DAY = NEXT_DAY.replace(hour=0, minute=0, second=0, microsecond=0)

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
                                   'sheets.googleapis.com-python-quickstart.json')

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

# print json.dumps(json_dict, indent=4, separators=(",",": "))

def parse(json_dict, values):
    if not values:
        print('No data found.')
    else:
        ROW_COUNT = 1
        REQ_COUNT = 0
        REQUISITION = None
        REQUISITION_TYPE = None
        DEGREE = None
        LOCATION = None
        NAME = None
        for row in values:
            # print(row)
            if ROW_COUNT == 1:
                REQUISITION_TYPE = row
                for item in REQUISITION_TYPE:
                    if item != u'':
                        REQ_COUNT += 1
                ROW_LENGTH = ((REQ_COUNT*5)-1) # No Whitespace Column at beginning or end
                if len(REQUISITION_TYPE) < ROW_LENGTH:
                    OFST = ROW_LENGTH - len(REQUISITION_TYPE)
                    REQUISITION_TYPE += [u''] * OFST
            elif ROW_COUNT == 2:
                DEGREE = row
                if len(DEGREE) < ROW_LENGTH:
                    OFST = ROW_LENGTH - len(DEGREE)
                    DEGREE += [u''] * OFST
                    # print(DEGREE)
            elif ROW_COUNT == 3:
                REQUISITION = row
                if len(REQUISITION) < ROW_LENGTH:
                    OFST = ROW_LENGTH - len(REQUISITION)
                    REQUISITION += [u''] * OFST
                    # print(REQUISITION)
            elif ROW_COUNT == 4:
                LOCATION = row
                if len(LOCATION) < ROW_LENGTH:
                    OFST = ROW_LENGTH - len(LOCATION)
                    LOCATION += [u''] * OFST
                    # print(LOCATION)
            elif ROW_COUNT >= 7:
                NAME = row
                if len(NAME) < ROW_LENGTH:
                    OFST = ROW_LENGTH - len(NAME)
                    NAME += [u''] * OFST
                    # print(NAME)
                for i in range(0,REQ_COUNT):
                    # print("REQ #%d" % (i+1))
                    # print("R1 " + NAME[i*5+1])
                    if NAME[i*5+1] != u'':
                        json_dict[0]["Locations"][LOCATION[i*5+1]]["Degrees"][DEGREE[i*5+1]][REQUISITION_TYPE[i*5]]["Requisitions"][REQUISITION[i*5+1]]["Round 1"].append(NAME[i*5+1])
                    # print("R2 " + NAME[i*5+2])
                    if NAME[i*5+2] != u'':
                        json_dict[0]["Locations"][LOCATION[i*5+1]]["Degrees"][DEGREE[i*5+1]][REQUISITION_TYPE[i*5]]["Requisitions"][REQUISITION[i*5+1]]["Round 2"].append(NAME[i*5+2])
                    # print("R3 " + NAME[i*5+3])
                    if NAME[i*5+3] != u'':
                        json_dict[0]["Locations"][LOCATION[i*5+1]]["Degrees"][DEGREE[i*5+1]][REQUISITION_TYPE[i*5]]["Requisitions"][REQUISITION[i*5+1]]["Round 3"].append(NAME[i*5+3])
            ROW_COUNT += 1
    return json_dict

def convert_worksheet(service, spreadsheetId, USArangeName, CHrangeName, NEXT_DAY):
    json_dict = json.loads(
        '''
        [
            {
                "Locations": {
                    "Chicago": {
                        "Degrees": {
                            "Undergraduate": {
                                "INTERN": {
                                    "Requisitions": {
                                        "RV Trader": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Algorithmic Trader": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Software Engineer": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "DevOps Engineer": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Systems Engineer": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Network Engineer": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Business Operations Associate": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Financial Analyst": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Legal Representative": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        }
                                    }
                                },
                                "FULL TIME": {
                                    "Requisitions": {
                                        "RV Trader": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Algorithmic Trader": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Software Engineer": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "DevOps Engineer": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Systems Engineer": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Network Engineer": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Business Operations Associate": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Financial Analyst": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Legal Representative": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        }
                                    }
                                }
                            },
                            "Graduate": {
                                "INTERN": {
                                    "Requisitions": {
                                        "RV Trader": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Algorithmic Trader": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Software Engineer": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "DevOps Engineer": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Systems Engineer": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Network Engineer": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Business Operations Associate": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Financial Analyst": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Legal Representative": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        }
                                    }
                                },
                                "FULL TIME": {
                                    "Requisitions": {
                                        "RV Trader": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Algorithmic Trader": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Software Engineer": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "DevOps Engineer": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Systems Engineer": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Network Engineer": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Business Operations Associate": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Financial Analyst": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Legal Representative": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "Martigny": {
                        "Degrees": {
                            "Undergraduate": {
                                "INTERN": {
                                    "Requisitions": {
                                        "RV Trader": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Algorithmic Trader": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Software Engineer": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "DevOps Engineer": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Systems Engineer": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Network Engineer": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Business Operations Associate": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Financial Analyst": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Legal Representative": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        }
                                    }
                                },
                                "FULL TIME": {
                                    "Requisitions": {
                                        "RV Trader": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Algorithmic Trader": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Software Engineer": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "DevOps Engineer": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Systems Engineer": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Network Engineer": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Business Operations Associate": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Financial Analyst": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Legal Representative": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        }
                                    }
                                }
                            },
                            "Graduate": {
                                "INTERN": {
                                    "Requisitions": {
                                        "RV Trader": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Algorithmic Trader": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Software Engineer": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "DevOps Engineer": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Systems Engineer": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Network Engineer": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Business Operations Associate": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Financial Analyst": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Legal Representative": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        }
                                    }
                                },
                                "FULL TIME": {
                                    "Requisitions": {
                                        "RV Trader": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Algorithmic Trader": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Software Engineer": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "DevOps Engineer": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Systems Engineer": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Network Engineer": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Business Operations Associate": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Financial Analyst": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        },
                                        "Legal Representative": {
                                            "Round 1": [],
                                            "Round 2": [],
                                            "Round 3": []
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        ]
        ''')
    result = service.spreadsheets().values().get(
    spreadsheetId=spreadsheetId, range=USArangeName).execute()
    values = result.get('values', [])

    json_dict = parse(json_dict, values)

    result = service.spreadsheets().values().get(
    spreadsheetId=spreadsheetId, range=CHrangeName).execute()
    values = result.get('values', [])

    json_dict = parse(json_dict, values)

    with open("interviewers-%s.json"%NEXT_DAY,"wb") as fh:
        print("Writing to interviewers-%s.json."%NEXT_DAY)
        fh.write(json.dumps(json_dict, indent=4, sort_keys=True, separators=(",",": ")))

def main():
    global CURRENT_DAY, NEXT_DAY
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '15QBvGEjoKl6Kb2VkV_e7ayUFRuDh_R7FC3BnJJE5fqY'
    USArangeName = '[USA] Assignee DB!A1:ZZ500'
    CHrangeName = '[CH] Assignee DB!A1:ZZ500'

    FIRST_DAY = datetime.datetime.now().replace(hour=0,minute=0,second=0,microsecond=0)
    convert_worksheet(service, spreadsheetId, USArangeName, CHrangeName, FIRST_DAY)

    while True:
        if datetime.datetime.now() > NEXT_DAY:
            convert_worksheet(service, spreadsheetId, USArangeName, CHrangeName, NEXT_DAY)
            if CURRENT_DAY != None:
                print("Removing interviewers-%s.json."%CURRENT_DAY)
                os.remove("interviewers-%s.json"%CURRENT_DAY)
            else:
                print("Removing interviewers-%s.json."%FIRST_DAY)
                os.remove("interviewers-%s.json"%FIRST_DAY)
            CURRENT_DAY = NEXT_DAY
            # NEXT_DAY = datetime.datetime.now() + datetime.timedelta(minutes=1)
            NEXT_DAY = datetime.datetime.now() + datetime.timedelta(days=1)
            # NEXT_DAY = NEXT_DAY.replace(second=0, microsecond=0)
            NEXT_DAY = NEXT_DAY.replace(hour=0, minute=0, second=0, microsecond=0)

if __name__ == '__main__':
	main()