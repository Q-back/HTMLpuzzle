import sys, os, glob, shutil, logging
from file_reader import FileReader
from base_file import BaseFile
from template_file import TemplateFile

class Render():

	arg = None
	base_file_path = None
	base_file = None
	working_dir = ""

	@classmethod
	def show_working_dir(self):
		return self.working_dir

	@classmethod
	def find_last_slash_in_str(self, string):
		string = string[::-1]
		for i in range (0, len(string) ): 
			if string[i] == "/":
				return -i

	def __init__(self, arg):
		self.arg = arg

	def start(self):
		logging.info("Start rendering")
	
		#python should open file in dir where command was launched, not dir where .py file actually is
	
		self.base_file_path = self.arg[1]
		self.base_file = BaseFile(self.base_file_path)		
		last_slash_in_file_path = self.find_last_slash_in_str(self.base_file_path)
		self.working_dir = self.base_file_path[0:last_slash_in_file_path]
		self.check_if_dirs_exsist()
		self.backup_old_files()
		for filename in glob.glob(self.working_dir + "*" + ".html"):
			#print(filename) #DEBUG
			if filename != self.base_file_path:
				self.__start_compare(filename)

	def __start_compare(self, filename):
		template_file = TemplateFile(filename)
		template_file.render(base_file=self.base_file)

	def check_if_dirs_exsist(self):
		if not (os.path.exists(self.working_dir+"rendered") and os.path.exists(self.working_dir+"backup")):
			logging.info("Creating project directories")
			self.create_project_dirs()

	def create_project_dirs(self):
		os.mkdir(self.working_dir+"rendered")
		os.mkdir(self.working_dir+"backup")

	def backup_old_files(self): 
		os.mkdir(self.working_dir+"tmp")
		os.rename(self.working_dir+"rendered/*", self.working_dir+"tmp/")
		# for backuped_filename in self.working_dir+"rendered/*":
		# 	os.rename(backuped_filename, 
		renamed_files = glob.glob(self.working_dir+"tmp/*")
		logging.debug("Moved files: %s",renamed_files)
		shutil.rmtree(self.working_dir+"backup")
		os.rename(self.working_dir+"tmp", self.working_dir+"backup")


	#def find_tag_in_file():	
