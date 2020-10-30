# GPL v3 or later
# author: Nic Freeman

# given a folder with template (.tex) marking files, and students (.pdf) work files:
# create one copy of each template for each student & name accordingly

import glob
import shutil

base_files = glob.glob("./*.tex")
pdf_files = glob.glob("./*.pdf")
all_files = glob.glob("./*")

student_names = []
for file in pdf_files:
	student_name = file.split(".")[1][1:]
	student_names.append(student_name)

# avoid fork bomb
pruned_base_files = []
for file in base_files:
	base_name = file.split(".")[1][1:]
	allow = True
	for student_name in student_names:
		if student_name in base_name:
			allow = False
			break
	if allow:
		pruned_base_files.append(base_name)
	
for file in pruned_base_files:	
	for student_name in student_names:
		out_file = "./" + student_name + "_" + file + ".tex"
		if out_file in all_files:
			print("skipped, exists already: %s" % out_file)
			continue
		print("writing: %s" % out_file)
		shutil.copyfile(file+".tex", out_file)