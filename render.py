import sys, os, glob, shutil, logging
from file_reader import FileReader
from base_file import BaseFile
from template_file import TemplateFile
from helpers.helper_files import HelperFiles

class Render():

	arg = None
	base_file_path = None
	base_file = None
	working_dir = ""

	@classmethod
	def get_working_dir_from_filepath(self, filepath):
		logging.debug("string to convert:"+filepath)
		filepath = filepath[::-1]
		for i in range (0, len(filepath) ): 
			if filepath[i] == "/":
				dir_path = filepath[i:]
				logging.debug("dir_path="+dir_path[::-1])
				return dir_path[::-1]

	def __init__(self, arg):
		self.arg = arg

	def start(self):
		logging.info("Starting")
	
		#python should open file in dir where command was launched, not dir where .py file actually is
	
		self.base_file_path = self.arg[1]
		self.base_file = BaseFile(self.base_file_path)
		self.working_dir = self.get_working_dir_from_filepath(self.base_file_path)
		logging.debug("working_dir="+self.working_dir)
		self.check_if_dirs_exsist()
		self.backup_old_files()
		logging.info("Starting render")
		for filename in glob.glob(self.working_dir + "*" + ".html"):
			if filename != self.base_file_path:
				self.__start_compare(filename)
		logging.info("Finished")

	def __start_compare(self, filename):
		template_file = TemplateFile(filename)
		self.base_file = BaseFile(self.base_file_path)
		template_file.render(base_file=self.base_file)

	def check_if_dirs_exsist(self):
		if not (os.path.exists(self.working_dir+"rendered") and os.path.exists(self.working_dir+"backup")):
			logging.info("Creating project directories")
			self.create_project_dirs()

	def create_project_dirs(self):
		os.mkdir(self.working_dir+"rendered")
		os.mkdir(self.working_dir+"backup")

	def backup_old_files(self):
		logging.info("Starting backup")
		try:
			shutil.rmtree(self.working_dir+"tmp")
			logging.warn("Removing tmp dir. Something must went wrong previously. Backup files may be lost.")
		except FileNotFoundError:
			pass
			logging.debug("rm tmp fine")

		os.mkdir(self.working_dir+"tmp")
		for backuped_filename in glob.glob(self.working_dir+"rendered/*"):
			logging.debug("backuped_filename="+backuped_filename)
			os.rename(backuped_filename, self.working_dir+"tmp/"+HelperFiles.get_filename_from_filepath(backuped_filename)) 
		renamed_files = glob.glob(self.working_dir+"tmp/*")
		logging.debug("Moved files: %s",renamed_files) # old-style formatting
		shutil.rmtree(self.working_dir+"backup")
		os.rename(self.working_dir+"tmp", self.working_dir+"backup")


	#def find_tag_in_file():	
