import logging
from file_reader import FileReader

class TemplateFile(FileReader):

	def render(self, base_file):
		self.new_file_path = self.create_new_file_path()
		base_file.write_until_tag(new_file_path=self.new_file_path, template=self)
		# repeat that until end of file
		# write new file until find tag in base file. Then match tag in template file, and countinue writing

	def write_tag_content(self, wanted_tag, file_to_write):
		self.tag = wanted_tag
		template_file = open(self.file_path, "r")
		next_tag = self.find_next_tag()
		if next_tag == False:
			logging.error("no matching tag found for: "+wanted_tag)
			self.add_tag_to_template(wanted_tag)
		elif next_tag == wanted_tag:
			logging.debug("found tag: "+wanted_tag)
			template_file.seek(self.file_seek_position)
			for line_text in template_file:
				if not self._check_if_line_is_endtag(line_text):
					file_to_write.write(line_text[0:-1]) # Can't render whole line cause \n at end
				else:
					break
		else:
			logging.debug("can't match '"+str(next_tag)+"' with '"+wanted_tag+ "'")
			self.write_tag_content(wanted_tag, file_to_write)
		template_file.close()

	def add_tag_to_template(self, wanted_tag):
		logging.debug("Opening template in path: "+self.file_path+" to add missing tag: "+wanted_tag)
		template_file = open(self.file_path, "a+")
		template_file.write("\n{%"+wanted_tag+"%}\n"+"{%/"+wanted_tag+"%}")
		template_file.close()
		logging.info("Added missing tag ("+wanted_tag+") to: "+self.file_path)

	def _check_if_line_is_endtag(self, line_text):
		# Checks if line contains MATCHING endtag
		tag_start_index = line_text.find("{%/")
		if tag_start_index > -1:
			endtag = line_text[tag_start_index+3:line_text.find("%}")]
			logging.debug("found endtag: "+endtag+" while tag is: "+str(self.tag))
			if endtag == self.tag:
				logging.debug("endtag match!")
				self._reset_tag_search_file_seeker_position()
				return True
		else:
			return False

	def _reset_tag_search_file_seeker_position(self):
		self.file_seek_position = 0
		logging.debug("File seeker position reset")