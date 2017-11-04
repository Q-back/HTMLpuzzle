import logging
from file_reader import FileReader

class BaseFile(FileReader):

	def write_until_tag(self, new_file_path, template):
		self.new_file_path = new_file_path
		new_file = open(self.new_file_path, "a+")
		base_file = open(self.file_path, "r")
		for line_text in base_file:
			if not self._check_if_line_is_tag(line_text):
				new_file.write(line_text)
			else:
				logging.debug("Rendering template tag")
				self.write_tag(line_text, new_file, template)
		new_file.close()
		base_file.close()
		logging.debug("File rendered to: "+self.new_file_path)

	def write_tag(self, line_text, file, template):
		template_starts = line_text.find("{%") # noob method to check if there is tag left in text
		if template_starts > -1:
			content_to_start_tag = line_text[:line_text.find("{%")]
			content_from_end_tag = line_text[line_text.find("%}")]
			file.write(content_to_start_tag)
			template.write_tag_content(self.tag, file)
			if self._check_if_line_is_tag(content_from_end_tag):
				self.write_tag(line_text, file, template) # There is another tag to render, so recurency
			else:
				file.write(content_from_end_tag)
				return 0

		else:
			return 0
