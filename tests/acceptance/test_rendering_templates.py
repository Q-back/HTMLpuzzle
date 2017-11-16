import os, shutil, sys, logging
from render import Render

class TestEveryTagOnceInRightOrder():
	logging.basicConfig(level=logging.DEBUG, format="(TEST)[%(levelname)s](%(module)s->%(funcName)s): %(message)s")
	@classmethod
	def setup_class(cls):
		try:
			os.mkdir("./test_tmp")
			base_file = open("./test_tmp/base.html", "w+")
			base_file.write(
				"some data"
				"\n{%first_tag%}\n"
				"\ndata after first tag"
				"\n{%second_tag%}\n"
				"\ndata after second tag"
				)
			base_file.close()
			templ_file = open("./test_tmp/templ_file.html", "w+")
			templ_file.write(
				"{%first_tag%}"
				"\nfirst thing"
				"\n{%/first_tag%}"
				"\n{%second_tag%}"
				"\nsecond thing"
				"\n{%/second_tag%}"
				)
			templ_file.close()
		except:
			print("Error during creating tmp dir:", sys.exc_info()[0])

	@classmethod
	def teardown_class(cls):
		#pass
		shutil.rmtree("./test_tmp")

	def test_it_can_create_proper_template_from_basic_file_with_fine_order_and_tags_once(self):
		render = Render(["zero_arg","./test_tmp/base.html"])
		render.start()
		rendered_file = open("./test_tmp/rendered/templ_file.html", "r")
		rendered_file_content = rendered_file.read()
		rendered_file.close()
		logging.debug("rendered file content: " + rendered_file_content)
		logging.debug("content we want have: " + "some data"
				"\nfirst thing"
				"\ndata after first tag"
				"\nsecond thing"
				"\ndata after second tag")
		assert rendered_file_content == (
				"some data"
				"\nfirst thing"
				"\ndata after first tag"
				"\nsecond thing"
				"\ndata after second tag"
				)