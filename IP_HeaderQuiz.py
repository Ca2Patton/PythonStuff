#!/usr/bin/python

QandA = {"What is the total byte size of an IP header? (excluding any options and data): " : 20, "What's the total bit size of each block in an IP header?: " : 32, "How many bits is the version?: " : 4, "What is the bit size of the header length?: " : 4, "What is the bit length of the type of service?: " : 8, "What bit size is the total length?: " : 16, "What is the bit size of the identification?: " : 16, "What is the length of the bit flags?: " : 3, "What is the length of the fragment offset in bits?: " : 13, "What is the bit size of the time to live?: " : 8, "What is the bit size of the protocol?: " : 8, "What is the bit size of the header checksum?: " : 16, "What is the bit length of the source ip address?: " : 32, "What is the bit length of the destination ip address?: " : 32}

question = QandA.keys()

for q in question:
	answer = raw_input(question)
	if answer == question:
		print "Correct!"
	else:
		print "Wrong!"
		break
