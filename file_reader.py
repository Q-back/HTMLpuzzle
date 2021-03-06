import logging, render
from helpers.helper_files import HelperFiles

class FileReader():

	file_path = None
	new_file_path = None
	file_seek_position = 0
	new_file_seek_position = 0
	tag = None

	def __init__(self, file_path):
		self.file_path = file_path

	def find_next_tag(self):
		file = open(self.file_path, "r")
		file.seek(self.file_seek_position)
		found_something = False
		line_text = file.readline()
		while line_text:
			tag = self._check_if_line_is_tag(line_text)
			if tag:
				found_something = True
				break
			line_text = file.readline()

		if found_something:
			self.file_seek_position = file.tell()
			logging.debug("found something at: "+str(self.file_seek_position)) #DEBUG
		else:
			logging.debug("nothing found in: "+ self.file_path) #DEBUG
			tag = False
		file.close()
		return tag

	def _check_if_line_is_tag(self, line_text):
		tag_start_index = line_text.find("{%")
		if tag_start_index > -1 and line_text[tag_start_index+2] != "/":
			tag = line_text[tag_start_index+2:line_text.find("%}")]
			logging.debug("line is tag: "+tag)
			return tag
		else:
			return False
		#pure_text = line_text = ''.join(line_text.split())

	def create_new_file_path(self):
		filename = HelperFiles.get_filename_from_filepath(self.file_path)
		logging.debug("new file path: "+render.Render.get_working_dir_from_filepath(self.file_path)+"rendered/"+filename)
		return render.Render.get_working_dir_from_filepath(self.file_path)+"rendered/"+filename

	def clear_file(self):
		logging.warning("to be implemented")

