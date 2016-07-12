from jira import JIRA
import gspread, json
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('myKeyfile.json', scope)

gc = gspread.authorize(credentials)

json_dict = json.loads(
'''
[
    {
        "Locations": {
            "Chicago": {
                "Degrees": {
                    "Undergraduate": {
                        "Intern": {
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
                        "Full Time": {
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
                        "Intern": {
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
                        "Full Time": {
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
                        "Intern": {
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
                        "Full Time": {
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
                        "Intern": {
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
                        "Full Time": {
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
# print json.dumps(json_dict, indent=4, separators=(",",": "))

def main():
    wks = gc.open("Prototyping Interview Database").worksheet('[USA] Assignee DB')

    # print wks.get_all_values
    ROWS = 50
    COLS = 4
    REQ_COUNT = 0
    C_IND = 1
    C_OFST = 0
    # print wks.cell(1,181).value == ""
    while wks.cell(1,C_IND+C_OFST).value != "":
        # print wks.cell(1,C_IND+C_OFST).value
        REQ_COUNT += 1
        C_OFST += 5
        # print REQ_COUNT
        # raw_input()
        # print wks.cell(1,C_IND+C_OFST).value == ""
    i = 1
    j = 1
    REQUISITION = ""
    # REQUISITION_TYPE = ""
    DEGREE = ""
    LOCATION = ""
    for k in range(0,REQ_COUNT):
        if k % 4 >= 2:
            continue
        for i in range(1,ROWS+1):
            for j in range(1,COLS+1):

                # print i *((j % 4) + 1) <= ROWS * COLS
                print "ROW: %d - COL: %d\n" % (i, j)

                if wks.cell(i,j+k*5).value != "":
                    # print "\t" + wks.cell(i,j).value

                    if i < 7:
                        if wks.cell(i,j+k*5).value == "DEGREE":
                            DEGREE = wks.cell(i,j+k*5+1).value
                            # print DEGREE
                            # raw_input()

                        if wks.cell(i,j+k*5).value == "REQUISITION":
                            REQUISITION = wks.cell(i,j+k*5+1).value
                            # print REQUISITION
                            # raw_input()

                        if wks.cell(i,j+k*5).value == "LOCATION":
                            LOCATION = wks.cell(i,j+k*5+1).value
                            # print LOCATION
                            # raw_input()
                    else:
                        if i == 7:
                            print REQUISITION, DEGREE, LOCATION
                        # print "GO"
                        # raw_input()
                        if j == 1:
                            continue
                        else:
                            json_dict[0]["Locations"][LOCATION]["Degrees"][DEGREE]["Intern"]["Requisitions"][REQUISITION]["Round %d"%(j-1)].append(
                                wks.cell(i,j+k*5).value
                                )
                            json_dict[0]["Locations"][LOCATION]["Degrees"][DEGREE]["Full Time"]["Requisitions"][REQUISITION]["Round %d"%(j-1)].append(
                                wks.cell(i,j+k*5).value
                                )
                            # print json.dumps(json_dict, indent=4, separators=(",",": "))
                            with open("interviewers-test.json","w") as fh:
                                fh.write(json.dumps(json_dict, indent=4, separators=(",",": ")))
    wks = gc.open("Prototyping Interview Database").worksheet('[CH] Assignee DB')
    ROWS = 50
    COLS = 4
    REQ_COUNT = 0
    C_IND = 1
    C_OFST = 0
    # print wks.cell(1,181).value == ""
    i = 1
    j = 1
    REQUISITION = ""
    REQUISITION_TYPE = ""
    DEGREE = ""
    LOCATION = ""
    while wks.cell(1,C_IND+C_OFST).value != "":
        # print wks.cell(1,C_IND+C_OFST).value
        REQ_COUNT += 1
        C_OFST += 5
    for k in range(0,REQ_COUNT):
        if k % 4 >= 2:
            continue
        for i in range(1,ROWS+1):
            for j in range(1,COLS+1):

                # print i *((j % 4) + 1) <= ROWS * COLS
                print "ROW: %d - COL: %d\n" % (i, j)

                if wks.cell(i,j+k*5).value != "":
                    # print "\t" + wks.cell(i,j).value

                    if i < 7:
                        if wks.cell(i,j+k*5).value == "DEGREE":
                            DEGREE = wks.cell(i,j+k*5+1).value
                            # print DEGREE
                            # raw_input()

                        if wks.cell(i,j+k*5).value == "REQUISITION":
                            REQUISITION = wks.cell(i,j+k*5+1).value
                            # print REQUISITION
                            # raw_input()

                        if wks.cell(i,j+k*5).value == "LOCATION":
                            LOCATION = wks.cell(i,j+k*5+1).value
                            # print LOCATION
                            # raw_input()
                    else:
                        if i == 7:
                            print REQUISITION, DEGREE, LOCATION
                        # print "GO"
                        # raw_input()
                        if j == 1:
                            continue
                        else:
                            json_dict[0]["Locations"][LOCATION]["Degrees"][DEGREE]["Intern"]["Requisitions"][REQUISITION]["Round %d"%(j-1)].append(
                                wks.cell(i,j+k*5).value
                                )
                            json_dict[0]["Locations"][LOCATION]["Degrees"][DEGREE]["Full Time"]["Requisitions"][REQUISITION]["Round %d"%(j-1)].append(
                                wks.cell(i,j+k*5).value
                                )
                            # print json.dumps(json_dict, indent=4, separators=(",",": "))
                            with open("interviewers-test.json","w") as fh:
                                fh.write(json.dumps(json_dict, indent=4, separators=(",",": ")))

if __name__ == '__main__':
	main()