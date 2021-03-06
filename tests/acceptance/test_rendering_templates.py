import os, shutil, sys, logging
from render import Render

logging.basicConfig(level=logging.DEBUG, format="(TEST)[%(levelname)s](%(module)s->%(funcName)s): %(message)s")

class RenderingTemplatesHelper():
	@classmethod
	def prepare_files(cls, base_file_content, templ_file_content):
		try:
			os.mkdir("./test_tmp")
			base_file = open("./test_tmp/base.html", "w+")
			base_file.write(base_file_content)
			base_file.close()
			templ_file = open("./test_tmp/templ_file.html", "w+")
			templ_file.write(templ_file_content)
			templ_file.close()
		except:
			print("Error during creating tmp dir:", sys.exc_info()[0])

	@classmethod
	def check_if_render_is_expected(cls, expected_content):
		render = Render(["zero_arg","-d", "./test_tmp/base.html"])
		render.start()
		rendered_file = open("./test_tmp/rendered/templ_file.html", "r")
		rendered_file_content = rendered_file.read()
		rendered_file.close()
		logging.debug("rendered file content: " + rendered_file_content)
		logging.debug("wanted content: " + expected_content)
		assert rendered_file_content == (expected_content)

class TestEveryTagOnceInRightOrder():
	@classmethod
	def setup_class(cls):
		base_file_content = (
				"some data"
				"\n{%first_tag%}\n"
				"\ndata after first tag"
				"\n{%second_tag%}\n"
				"\ndata after second tag"
				)
		templ_file_content = (
				"{%first_tag%}"
				"\nfirst thing"
				"\n{%/first_tag%}"
				"\n{%second_tag%}"
				"\nsecond thing"
				"\n{%/second_tag%}")
		RenderingTemplatesHelper.prepare_files(base_file_content=base_file_content,
			templ_file_content=templ_file_content)
	@classmethod
	def teardown_class(cls):
		shutil.rmtree("./test_tmp")

	def test_it_can_create_proper_template_from_basic_file_with_fine_order_and_tags_once(self):
		expected_content = (
				"some data"
				"\nfirst thing"
				"\ndata after first tag"
				"\nsecond thing"
				"\ndata after second tag"
				)
		RenderingTemplatesHelper.check_if_render_is_expected(expected_content=expected_content)

class TestTagsInWrongOrder():
	@classmethod
	def setup_class(cls):
		base_file_content = (
				"some data"
				"\n{%first_tag%}\n"
				"\ndata after first tag"
				"\n{%second_tag%}\n"
				"\ndata after second tag"
				)
		templ_file_content = (
				"{%second_tag%}"
				"\nsecond thing"
				"\n{%/second_tag%}"
				"\n{%first_tag%}"
				"\nfirst thing"
				"\n{%/first_tag%}"
				)
		RenderingTemplatesHelper.prepare_files(base_file_content, templ_file_content)
	@classmethod
	def teardown_class(cls):
		shutil.rmtree("./test_tmp")

	def test_it_can_create_template_with_wrong_tag_order(self):
		expected_content = (
			"some data"
			"\nfirst thing"
			"\ndata after first tag"
			"\nsecond thing"
			"\ndata after second tag"
			)
		RenderingTemplatesHelper.check_if_render_is_expected(expected_content=expected_content)

class TestMultipleSameTag():
	@classmethod
	def setup_class(cls):
		base_file_content = (
				"some data"
				"\n{%first_tag%}\n"
				"\ndata after first tag"
				"\n{%first_tag%}\n"
				"\ndata after first tag again"
				"\n{%second_tag%}\n"
				"\ndata after second tag"
				)
		templ_file_content = (
				"{%first_tag%}"
				"\nfirst thing"
				"\n{%/first_tag%}"
				"\n{%second_tag%}"
				"\nsecond thing"
				"\n{%/second_tag%}"
				)
		RenderingTemplatesHelper.prepare_files(base_file_content, templ_file_content)
	@classmethod
	def teardown_class(cls):
		shutil.rmtree("./test_tmp")

	def test_it_can_create_template_with_wrong_tag_order(self):
		expected_content = (
			"some data"
			"\nfirst thing"
			"\ndata after first tag"
			"\nfirst thing"
			"\ndata after first tag again"
			"\nsecond thing"
			"\ndata after second tag"
			)
		RenderingTemplatesHelper.check_if_render_is_expected(expected_content=expected_content)

class TestMixed():
	@classmethod
	def setup_class(cls):
		base_file_content = (
				"some data"
				"\n{%first_tag%}\n"
				"\ndata after first tag"
				"\n{%first_tag%}\n"
				"\ndata after first tag again"
				"\n{%second_tag%}\n"
				"\ndata after second tag"
				)
		templ_file_content = (
				"\n{%second_tag%}"
				"\nsecond thing"
				"\n{%/second_tag%}"
				"\n{%first_tag%}"
				"\nfirst thing"
				"\n{%/first_tag%}"
				)
		RenderingTemplatesHelper.prepare_files(base_file_content, templ_file_content)
	@classmethod
	def teardown_class(cls):
		shutil.rmtree("./test_tmp")

	def test_it_can_create_template_with_wrong_tag_order_and_one_tag_used_two_times(self):
		expected_content = (
			"some data"
			"\nfirst thing"
			"\ndata after first tag"
			"\nfirst thing"
			"\ndata after first tag again"
			"\nsecond thing"
			"\ndata after second tag"
			)
		RenderingTemplatesHelper.check_if_render_is_expected(expected_content=expected_content)

class TestAutomaticTagCreationInTemplateFile():
	@classmethod
	def setup_class(cls):
		base_file_content = (
				"some data"
				"\n{%first_tag%}\n"
				"\ndata after first tag"
				"\n{%second_tag%}\n"
				"\ndata after second tag"
				)
		templ_file_content = (
				"\n{%second_tag%}"
				"\nsecond thing"
				"\n{%/second_tag%}"
				)
		RenderingTemplatesHelper.prepare_files(base_file_content, templ_file_content)
	@classmethod
	def teardown_class(cls):
		shutil.rmtree("./test_tmp")

	def test_it_add_tag_which_exist_only_in_base_to_template(self):
		expected_content = ("\n{%second_tag%}"
				"\nsecond thing"
				"\n{%/second_tag%}"
				"\n{%first_tag%}"
				"\n{%/first_tag%}")

		render = Render(["zero_arg","-d", "./test_tmp/base.html"])
		render.start()

		template_file = open("./test_tmp/templ_file.html", "r")
		template_file_content = template_file.read()
		template_file.close()

		logging.debug("template file content: " + template_file_content)
		logging.debug("wanted content: " + expected_content)

		assert template_file_content == expected_content

class TestMultipleTagsInSameLine():
	@classmethod
	def setup_class(cls):
		base_file_content = (
				"some data"
				"\n{%first_tag%}\n"
				"\ndata after first tag"
				"data before first tag inline {%first_tag%} data after first tag inline, data before second tag inline{%second_tag%}data after second tag inline, data before third tag inline {%third_tag%} data after inline"
				"\n{%second_tag%}\n"
				"\ndata after second tag"
				)
		templ_file_content = (
				"\n{%second_tag%}"
				"\nsecond thing"
				"\n{%/second_tag%}"
				"\n{%first_tag%}"
				"\nfirst thing"
				"\n{%/first_tag%}"
				"\n{%third_tag%}"
				"\nthird thing"
				"\n{%/third_tag%}"
			)
		RenderingTemplatesHelper.prepare_files(base_file_content, templ_file_content)
	def teardown_class(cls):
		shutil.rmtree("./test_tmp")

	def test_it_can_render_mutliple_tags_in_same_line(self):
		expected_content = (
				"some data"
				"\nfirst thing"
				"\ndata after first tag"
				"data before first tag inline first thing data after first tag inline, data before second tag inlinesecond thingdata after second tag inline, data before third tag inline third thing data after inline"
				"\nsecond thing"
				"\ndata after second tag"
				)
		RenderingTemplatesHelper.check_if_render_is_expected(expected_content=expected_content)