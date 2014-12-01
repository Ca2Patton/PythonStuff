#!/usr/bin/python
import re
import sys

new_input = sys.argv[1]
numbers = False
letters = False

for i in new_input:
	if i.isdigit():
		numbers = i
	else:
		letters = i
	if numbers and letters:
		print letters * int(numbers)
		numbers = False
		letters = False
