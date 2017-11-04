import logging
#move Render.get_working_dir_from_filepath() here

class HelperFiles():
	@classmethod
	def get_filename_from_filepath(self, filepath):
		logging.debug("string to convert:"+filepath)
		filepath = filepath[::-1]
		for i in range (0, len(filepath) ): 
			if filepath[i] == "/":
				filepath = filepath[::-1]
				filename = filepath[-i:]
				logging.debug("filename="+filename)
				return filename