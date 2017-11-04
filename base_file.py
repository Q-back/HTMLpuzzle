import logging
from file_reader import FileReader

class BaseFile(FileReader):

	def write_until_tag(self, new_file_path):
		self.new_file_path = new_file_path
		new_file = open(self.new_file_path, "a+")
		base_file = open(self.file_path, "r")
		for line_text in base_file:
			if not self._check_if_line_is_tag(line_text):
				new_file.write(line_text)
			else:
				logging.warning("to be implemented")
		new_file.close()
		base_file.close()
		logging.debug("File rendered to: "+self.new_file_path)