#!/usr/bin/python
import sys

#variables
new_input = sys.argv[1]
counter = 0

#initialize for loop
for i in new_input:
	if counter % 2:
		print int(new_input[counter]) * new_input[counter - 1]
	counter += 1
