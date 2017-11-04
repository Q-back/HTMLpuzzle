import logging
from file_reader import FileReader

class TemplateFile(FileReader):

	def render(self, base_file):
		self.new_file_path = self.create_new_file_path()
		base_file.write_until_tag(new_file_path=self.new_file_path, template=self)
		# write new file until find tag in base file. Then match tag in template file, and countinue writing

	def write_tag_content(self, wanted_tag, file_to_write):
		template_file = open(self.file_path, "r")
		if self.find_next_tag() == wanted_tag:
			logging.debug("found tag: "+wanted_tag)
			template_file.seek(self.file_seek_position)
			for line_text in template_file:
				if not self._check_if_line_is_endtag(line_text):
					file_to_write.write(line_text)
				else:
					break
		template_file.close()


	def _check_if_line_is_endtag(self, line_text):
		# Checks if line contains MATCHING endtag
		tag_start_index = line_text.find("{%/")
		if tag_start_index > -1:
			endtag = line_text[tag_start_index+3:line_text.find("%}")]
			logging.debug("found endtag: "+endtag)
			if endtag == self.tag:
				return True
		else:
			return False
		logging.warning("To be implemented")