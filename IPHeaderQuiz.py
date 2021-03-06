#!/usr/bin/python

user = raw_input("Hello! What's your name?: ")
print "Hi, " + user + "!"

print "This is a quiz on the contents of an IP header. It's purpose is to help you memorize their content."

header = int(raw_input("What is the total byte size of an IP header? (excluding any options and data): "))
if header == 20:
	print "That's correct!"
else:
	print "Wrong!"

iph_block_length = int(raw_input("What's the total bit size of each block in an IP header?: "))
if iph_block_length == 32:
	print "That's correct!"
else:
	print "Wrong!"

version_length = int(raw_input("How many bits is the version?: "))
if version_length == 4:
	print "Correct!"
else:
	print "Wrong!"

TOS_length = int(raw_input("What is the bit length of the type of service?: "))
if TOS_length == 8:
	print "Correct!"
else:
	print "Wrong!"

total_length = int(raw_input("What bit size is the total length?: "))
if total_lenth == 16:
	print "Correct!"
else:
	print "Wrong!"

identification = int(raw_input("What is the bit size of the identification?: "))
if identification == 16:
	print "Correct!"
else:
	print "Wrong!"

bit_flags = int(raw_input("What is the length of the bit flags?: "))
if bit_flags == 3:
	print "Correct!"
else:
	print "Wrong!"

frag_offset = int(raw_input("What is the length of the fragment offset in bits?: "))
if frag_offset == 13:
	print "Correct!"
else:
	print "Wrong!"

time_to_live = int(raw_input("What is the bit size of the time to live?: "))
if time_to_live == 8:
	print "Correct!"
else:
	print "Wrong!"

checksum = int(raw_input("What is the bit size of the header checksum?: "))
if checksum == 16:
	print "Correct!"
else:
	print "Wrong!"

source_ip = int(raw_input("What is the bit length of the source ip address?: "))
if source_ip == 32:
	print "Correct!"
else:
	print "Wrong!"

destination_ip = int(raw_input("What is the bit length of the destination ip address?: "))
if destination_ip == 32:
	print "Correct!"
else:
	print "Wrong!"
