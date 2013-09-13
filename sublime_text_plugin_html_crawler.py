# parse the naoqi documentation and creates a text file suitable for creating a Sublime Text plugin
# Mike McFarlane
# v0-1: 23 Aug 2013, crawl docs and build a list of methods, classes and frameworks

"""look for <dl class="function"> for the start of each method """
""" then get everything between <dt and </dt> """
"""look for first instance of <a class="reference internal" href="../stdtypes.html# then title=" for return type """
"""look for <tt class="descclassname"> for class """
"""look for <tt class="descname"> for methods """
"""look for second instance of <a class="reference internal" for arguments """

import fnmatch
import os
 

def get_html_file_list():
	"""finds all the HTML API docs in a defined folder"""
	"""returns the list of html files as a list and writes them to a file"""

	PATH = '/Users/mikemcfarlane/Desktop/NAO_doc/doc-release-1.14-public/naoqi'
	pattern = '*api*.html'

	f = open("html_list.txt", "w")
	html_list = []
	 
	for root, dirs, files in os.walk(PATH):
	    for filename in fnmatch.filter(files, pattern):
	        #print (os.path.join(root, filename))
	        f.write((os.path.join(root, filename)) + "\n")
	        html_list.append((os.path.join(root, filename)))
	f.close()
	return html_list

def find_methods(html_list):
	"""crawl all the html api docs and create a list with all the methods in"""
	"""returns the methods list still in html tagged form"""

	file_dump = open("file_dump.txt", "w")

	methods_html = []
	for api_file in html_list:
		try:
			f = open(api_file, "r")			
		except:
			print "Error finding: " + api_file
			return None
		file_contents = f.read()
		index = 0
		while True:
			start_method = file_contents.find("""<dl class="function">""", index)
			if start_method == -1:
				break
			else:
				start_dt_tag = file_contents.find("<dt", start_method)
				end_dt_tag = file_contents.find("</dt>", start_dt_tag)
				method_info = file_contents[start_dt_tag + 4:end_dt_tag]
				methods_html.append("--" + api_file + "--" + method_info)
				index = end_dt_tag
				#file_dump.write(api_file +  "\n")
				file_dump.write("--" + api_file + "--" + method_info + "\n\n")				
		f.close()
	file_dump.close()
	return methods_html

def build_methods_dictionary(methods_html):
	"""build a dictionary of relevant info for each method"""
	"""return a dictionary"""
	methods_dictionary = {}
	

	for i in methods_html:
		index = 0
		method_syntax_list = ()
		return_type = ""
		argument0 = ""
		argument1 = ""
		argument2 = ""
		argument3 = ""
		argument4 = ""
		argument5 = ""
		argument6 = ""
		argument7 = ""
		argument8 = ""
		argument9 = ""
		#find framework name
		start_framework = i.find("/naoqi/", 0) + len('/naoqi/')
		end_framework = i.find("/", start_framework)
		framework = i[start_framework:end_framework].upper()
		print framework
		#find class::method to use as key
		start_class_method = i.find('''id="''', end_framework) + len('''id="''')
		end_class_method = i.find(">", start_class_method) - 1
		class_method = i[start_class_method:end_class_method]
		print class_method
		#find class name
		start_class_name = i.find('''<tt class="descclassname">''', end_class_method) + +len('''<tt class="descclassname">''')
		end_class_name = i.find("::</tt>", start_class_name)
		class_name = i[start_class_name:end_class_name].upper()
		print class_name
		#find method
		start_method_name = i.find('''<tt class="descname">''', end_class_name) + len('''<tt class="descname">''')
		end_method_name = i.find("</tt>", start_method_name)
		method_name = i[start_method_name:end_method_name]
		print method_name
		#find return type and arguments
		while True:
			index = i.find('''<a class="reference internal"''', index) 
			if index == -1:
				print "Done"
				break
			else:
				# use fnmatch for a wildcard
				start_return_type = i.find('''title="''', index) + len('''title="''')
				end_return_type = i.find('''">''', start_return_type)
				return_type = i[start_return_type:end_return_type]
				index = end_return_type
				print return_type


		
html_list = get_html_file_list()
methods_html = find_methods(html_list)
build_methods_dictionary(methods_html)







