import sys, os, glob

def main(arg):

	#python should open file in dir where command was launched, not dir where .py file actually is

	directory_with_templates = arg[1]
	for filename in glob.glob(directory_with_templates + "*"):
		print(filename)

main(sys.argv)