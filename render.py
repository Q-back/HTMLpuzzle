import sys, os, glob
from file_reader import FileReader

class Render():

	arg = None
	base_file_path = None

	def __init__(self, arg):
		self.arg = arg

	def start(self):
	
		#python should open file in dir where command was launched, not dir where .py file actually is
	
		self.base_file_path = self.arg[1]
		last_slash_in_file_path = self.__find_last_slash_in_str(self.base_file_path)
		directory_with_templates = self.base_file_path[0:last_slash_in_file_path]
		#print(directory_with_templates) #DEBUG
		for filename in glob.glob(directory_with_templates + "*" + ".html"):
			#print(filename) #DEBUG
			if filename != self.base_file_path:
				self.__start_compare(filename)

	def __find_last_slash_in_str(self, string):
		string = string[::-1]
		for i in range (0, len(string) ): 
			if string[i] == "/":
				return -i

	def __start_compare(self, filename):
		base_file = FileReader(filename)
		base_file.find_next_tag()

	#def find_tag_in_file():	
