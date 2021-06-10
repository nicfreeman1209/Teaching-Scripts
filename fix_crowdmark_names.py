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
	try:
		f = file[:-10]
		print(file)
		f, email = f.rsplit("_", 1)
		surname, forename = f.split("_", 1)
		email += ".ac.uk"
		reg = students[email]
		print(forename, surname, email, reg)
		os.rename(file, reg + ".pdf")
	except:
		print("WARNING:", file)