import json, random
def get_interviewer(my_list):
	num_interviewers = len(my_list)
	interviewer_index = random.randint(0,num_interviewers-1)
	return my_list[interviewer_index]


def main():
	with open('interviewers.json', 'rb') as fh:
		my_dict = json.load(fh)

	# print json.dumps(my_dict, indent=4, sort_keys=True, separators=(",", ": "))
	print 'Round 1: ' + get_interviewer(my_dict[0]['Intern'][0]['Trader']['Round1'])
	print 'Round 2: ' + get_interviewer(my_dict[0]['Intern'][0]['Trader']['Round2'])
	print 'Round 3: ' + get_interviewer(my_dict[0]['Intern'][0]['Trader']['Round3'])

if __name__ == "__main__":
	main()