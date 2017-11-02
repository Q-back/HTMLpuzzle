from file_reader import FileReader

class TemplateFile(FileReader):

	def render(self, base_file):
		self.new_file_path = self.create_new_file_path()
		base_file.write_until_tag(self.new_file_path)
		# write new file until find tag in base file. Then match tag in template file, and countinue writing