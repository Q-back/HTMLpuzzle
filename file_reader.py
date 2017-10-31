class FileReader():

	file_path = None
	file_position = 0
	tag = None

	def __init__(self, file_path):
		self.file_path = file_path

	def find_next_tag(self):
		file = open(self.file_path, "r")
		file.seek(self.file_position)
		for line_text in file:
			if self.__check_if_line_is_tag(line_text):
				print("found something") #DEBUG
				break
		print("nothing found in "+ self.file_path) #DEBUG
		file.close()

	def __check_if_line_is_tag(self, line_text):
		pure_text = line_text = ''.join(line_text.split())

		if len(pure_text)>4:
			if pure_text[0] == "{" and pure_text[1] == "%":
				self.tag = pure_text[2:-2]
				print(self.tag)
				return True
			else:
				return False
		else:
			return False

