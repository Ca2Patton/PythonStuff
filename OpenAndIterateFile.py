#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
import re

filename = open('/Users/Caitlin/foo.txt', "r")


for line in filename:
	m = re.search('^(\w+\s\w+)', line)
	if m:
		print "{}".format( m.group(1) )

filename.close

