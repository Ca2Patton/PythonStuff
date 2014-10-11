#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

fileString = open('/Users/Caitlin/scripts/python/randomText.txt', 'r')
line = fileString.readline()

while line:
	output = []
	words = line.split()
	for word in words:
		word = word.capitalize()
		output.append(word)
	newline = ' '.join(output)
	print newline
	line = fileString.readline()

