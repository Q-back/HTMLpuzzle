from render import Render

def setup_module(module):
	pass

def teardown_module(module):
	pass

def test_if_it_accepts_console_args_correctly():
	render = Render("--debug ./demo_templates/base.html")
	render.start()