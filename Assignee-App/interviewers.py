import json, random, datetime
CURRENT_DATE = datetime.datetime.now().replace(hour=0,minute=0,second=0,microsecond=0)
def get_interviewer(my_list):
	num_interviewers = len(my_list)
	interviewer_index = random.randint(0,num_interviewers-1)
	return my_list[interviewer_index]


def main():
	global CURRENT_DATE
	with open('interviewers-%s.json'%CURRENT_DATE, 'rb') as fh:
		my_dict = json.load(fh)

	# print json.dumps(my_dict, indent=4, sort_keys=True, separators=(",", ": "))
	print 'Round 1: ' + get_interviewer(my_dict[0]["Locations"]["Chicago"]["Degrees"]["Undergraduate"]["FULL TIME"]["Requisitions"]["RV Trader"]["Round 1"])
	print 'Round 2: ' + get_interviewer(my_dict[0]["Locations"]["Chicago"]["Degrees"]["Undergraduate"]["FULL TIME"]["Requisitions"]["RV Trader"]["Round 2"])
	print 'Round 3: ' + get_interviewer(my_dict[0]["Locations"]["Chicago"]["Degrees"]["Undergraduate"]["FULL TIME"]["Requisitions"]["RV Trader"]["Round 3"])

if __name__ == "__main__":
	main()