import csv, math
from random import shuffle

GRADERS = ['many_blocked', 'some_blocked', 'none_blocked']
HANDINS_FILENAME = '../submission_lists/example_assignment_submissions.csv'
OUTPUT_FILENAME = '../grading_assignments/test.csv'

def get_complete_handins_list(handins_filename):
	handins = []
	with open(handins_filename) as handins_csv:
		handins_reader = csv.reader(handins_csv, delimiter=',')
		for handin in handins_reader:
			handins.append((handin[0], handin[1])) # student email, student name
	return handins

def get_number_of_handins_per_ta(graders, handins):
	return math.ceil(len(handins) / len(graders))

def get_grader_blocklist(grader):
	blocklist_filename = '../ta_blocklists/' + grader + '_blocklist.csv'
	blocklisted_students = []
	with open(blocklist_filename) as blocklist_csv:
		blocklist_reader = csv.reader(blocklist_csv, delimiter=',')
		for student_email in blocklist_reader:
			blocklisted_students.append(student_email[0])
	return blocklisted_students

def construct_graders_blocklist_dict():
	blocklist_dict = {}
	for grader in GRADERS:
		blocklist_dict[grader] = get_grader_blocklist(grader)
	return blocklist_dict

def assign_grading():
	# We have to copy because these lists are going to get edited, and we want
	# to compare with the originals at the end for confirmation.
	remaining_graders = GRADERS[:]
	remaining_handins = get_complete_handins_list(HANDINS_FILENAME)[:]
	max_num_of_assignments = get_number_of_handins_per_ta(GRADERS, remaining_handins)
	blocklist_dict = construct_graders_blocklist_dict()

	# Shuffle the TA list so TAs don't get the same students every time.
	shuffle(remaining_graders)

	handins_that_have_been_assigned = []
	grader_assignments = {}
	for grader in remaining_graders:
		if grader not in grader_assignments:
			grader_assignments[grader] = []

	# while len(remaining_handins) > 0:
	for handin in remaining_handins:
		for grader in remaining_graders:
			if len(grader_assignments[grader]) >= max_num_of_assignments:
				remaining_graders.remove(grader)

			if handin[0] not in blocklist_dict[grader]:
				grader_assignments[grader].append(handin)
				handins_that_have_been_assigned.append(handin)
				break

	if len(handins_that_have_been_assigned) < len(remaining_handins):
		print("WARNING: not all handins have been assigned graders! The remaining handins are:\n")
		for handin in set(remaining_handins) - set(handins_that_have_been_assigned):
			print("STUDENT NAME: " + handin[1] + "     STUDENT EMAIL: " + handin[0])
		print("\nFirst, try running this script again. If there's still unassigned students,"
			+ " consider manually assigning these students in the completed assignments file.")
	return grader_assignments

def output_grading_assignments(grader_assignments):
	assignments_file = open(OUTPUT_FILENAME, "w")
	for grader in GRADERS:
		assignments_file.write(grader + "'s Assignments:\n")
		for student in grader_assignments[grader]:
			assignments_file.write(student[1] + '\n') # writes student's name
		assignments_file.write('\n\n')
	assignments_file.close()
	print("Grading assignments have been written to " + OUTPUT_FILENAME + ".")

def main():
	assigned_grading = assign_grading()
	output_grading_assignments(assigned_grading)
main()