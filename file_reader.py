import render

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
		for line_text in file:
			if self._check_if_line_is_tag(line_text):
				print("found something") #DEBUG
				break
		print("nothing found in "+ self.file_path) #DEBUG
		file.close()

	def _check_if_line_is_tag(self, line_text):
		tag_start_index = line_text.find("{%")
		if tag_start_index > -1:
			self.tag = line_text[tag_start_index+1:line_text.find("%}")]
			return True
		else:
			return False
		#pure_text = line_text = ''.join(line_text.split())

	def create_new_file_path(self):
		filename = self.file_path[render.Render.find_last_slash_in_str(self.file_path):]
		return render.Render.show_working_dir()+"rendered/"+filename

	def clear_file(self):
		print("FileRender.clear_file() -> to be implemented")

