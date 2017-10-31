import sys, os, glob

class Render():
	arg = None
	def __init__(self, arg):
		self.arg = arg

	def start(self):
	
		#python should open file in dir where command was launched, not dir where .py file actually is
	
		base_file_path = self.arg[1]
		last_slash_in_file_path = self.__find_last_slash_in_str(base_file_path)
		directory_with_templates = base_file_path[0:last_slash_in_file_path]
		print(directory_with_templates) #DEBUG
		for filename in glob.glob(directory_with_templates + "*"):
			print(filename) #DEBUG

	def __find_last_slash_in_str(self, string):
		string = string[::-1]
		for i in range (0, len(string) ): 
			if string[i] == "/":
				return -i

	#def find_tag_in_file():	
