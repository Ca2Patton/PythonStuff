#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

userInput = raw_input("File name? Please be specific about the file's location: ")
if userInput == '-':
	userInput = raw_input("Please input text. Afterward, press ENTER. ")
	userData = len(userInput)
	print userData
	counter = userInput.count(raw_input("Letter? "))
	print counter
else:
	try:
		with open(userInput, 'r') as f:
			read_data = f.read()
			f.close()
	except IOError:
		print "Cannot open file. Either the file name is invalid, or you do not have permission to open the file."
	else:
		numbers = len(read_data)
		print numbers
		counting = read_data.count(raw_input("Letter? "))
		print counting
