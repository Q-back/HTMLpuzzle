from render import Render

def setup_module(module):
	pass

def teardown_module(module):
	pass

def test_if_it_accepts_console_args_correctly():
	render = Render(["zero_arg","--debug ./wrong_dir/base.html"])
	
def test_it_accepts_normal_string():
	render = Render(["zero_arg","normal_string"])