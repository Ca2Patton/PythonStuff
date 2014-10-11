#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import re

string = "Put some text in here"

variable = re.search(r"""(
		e   #Match the letter e.
		\s  #Followed by a space.
		)""", string, re.VERBOSE)

if variable:
	print variable.group(1)
