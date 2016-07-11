import zipfile
import time
import sys
import os

# ISSUE: only works when word is in one block. If no replacement, need to copy and paste placeholder in

# Works when files have path: /home/some/files/documents/templates/{template}
# Will create a directory with path: /home/some/files/documents/complete

# In case any field has no value, allows to be fixed by hand
EMPTY_FIELD = "_______________"

PATH_TO_DOCS = "/home/tmgaws/TMG-ATS-PROJECT/documents"

def create_document(template, placeholders):
	# Get first and last name from sys arguments

	date = time.strftime("%d/%m/%y")
	placeholders["DATE"] = date

	# Open files needed to autocomplete
	template_file = os.path.join("%s"%(PATH_TO_DOCS), "templates", "%s.docx"%(template))
	if not os.path.exists(os.path.join("%s"%(PATH_TO_DOCS), "complete")):
		os.makedirs(os.path.join("%s"%(PATH_TO_DOCS), "complete"))

	# deletes file if it already exists, and then rewrites file
	name_of_file = "%s_%s_%s.docx"%(template, placeholders.get("FIRST"), placeholders.get("LAST"))
	os.remove(os.path.join("%s"%(PATH_TO_DOCS), "complete", name_of_file))
	edited_file = os.path.join("%s"%(PATH_TO_DOCS), "complete", ))

	# unzip the files
	template_doc = zipfile.ZipFile(template_file)
	edited_doc = zipfile.ZipFile(edited_file, "w")

	# Go through all files and replace based on placeholders dictionary
	for file in template_doc.filelist:
		template_text = template_doc.read(file)

		for key in placeholders.keys():
			# Annoying formatting to make it show up in bold (could be easier way, but I'm not sure bc word sucks)
			if(placeholders[key] == ""):
				placeholders[key] = EMPTY_FIELD
			template_text = template_text.replace(str("{%s}"%(key)), str(("</w:t></w:r><w:r><w:rPr><w:b/></w:rPr><w:t>%s")%(placeholders[key])))
		edited_doc.writestr(file.filename, template_text)

	template_doc.close()
	edited_doc.close()
	#print os.path.exists(os.path.join("%s"%(PATH_TO_DOCS), "complete"))
	#print "Edit complete."

def test_create_document():
	create_document("Testing", {"EMPLOYEE" : "Daniel Smith", "FIRST" : "Daniel", "LAST" : "SMITH"})

#test_create_document()