#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
#import pdb; pdb.set_trace()

my_string = raw_input("Please enter a letter and a number in succession. Ex: a1b4c2h5: ")
output = list(my_string)
print output
counter = 0
number_letter = []
for i in output:
	if counter % 2 == 0:
		pass
	else:
		#number_letter.append((int(output[counter]) * output[counter - 1]))
		number = int(output[counter])
		letter = output[counter - 1]
		number_letter.append(number * letter)
	counter += 1
concat = ''.join(number_letter)
print concat
