import glob
import os
import csv

# renames Crowdmarks pdfs to registration numbers

# needs an extract from CIES containing: forename, surname, reg, email
# placed next to this file, in same dir as scripts

students = {} # email -> reg
with open('cies_mime.unit_student_profile') as students_file:                                                                                          
	students_csv = csv.reader(students_file, delimiter='\t')
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