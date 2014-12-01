import sys

def lettersMultiply(printer):
	data = []
	counter = 0
	for i in printer:
		if counter % 2:
			data.append(int(printer[counter]) * printer[counter - 1])
		counter += 1
	return "".join(data)
