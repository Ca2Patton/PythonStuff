#!/usr/bin/python
#Packet Sniffer in Python
#For Linux

import socket

#Create an INET, raw socket

sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

#Receive a Packet
while True:
	print sock.recvfrom(80)
