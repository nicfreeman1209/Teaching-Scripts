import glob
import os
import csv

# take an extract from CIES containing: forename, surname, reg, email
# place next to this file, in same dir as scripts

students = {} # email -> reg
with open('cies_mime.unit_student_profile') as students_file:                                                                                          
	students_csv = csv.reader(students_file, delimiter='\t')
	(students_csv)
	for line in students_csv:
		students[line[3].lower()] = line[2]

files = glob.glob("*.pdf")
for file in files:
	s = file.split("_")
	forename = s[0]
	surname = s[1]
	email =s[2] + ".ac.uk"
	reg = students[email]
	os.rename(file, reg + ".pdf")