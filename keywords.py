#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import keyword


while True:
	try:
		word = raw_input("Enter a word: ")
		if keyword.iskeyword(word) == True:
			print "You have entered a python keyword."
		else:
			print "You have not entered a python keyword."
	except EOFError:
		print "Exiting"
		break


