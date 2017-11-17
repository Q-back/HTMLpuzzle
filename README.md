# HTMLpuzzle

HTMLpuzzle is simple framework which can boost e.g. creating static websites with large number of sub-pages.

Usage is simple.
- create basic file -> in basic file you can create tags like that: {%tag%}. There is no difference if it is newlined or inline
- create some template files, which will define how to fill your tags in base file. Those template files have to be in same dir as basic file
- now you should see tags in your template files. Fill them with content you want to have there and:
- run *python3 main.py path/to/basic_file.html*
- you can find rendered files in *path/to/rendered/*. Rendered files have same names as template files.
