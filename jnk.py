#!/opt/local/bin/python

import socket
import sys

#Define the hosts and create the scoket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Created socket"
host = socket.gethostname()
port = 12345

#Bind the socket
try:
	sock.bind((host, port))
#Throw an error if it fails
except socket.error as msg:
	print "Bind failed. Error Code: " + str(msg[0]) + " Message: " + msg[1]
	sys.exit()
print "Socket successfully bound"

#Start listening
sock.listen(10)
print "Listening..."

#Talk at the client
while 1:
	conn, addr = sock.accept()
	while True:
		print "Connected to " + addr[0] + ':' + str(addr[1])
		conn.send('Thank you for connecting!')
		data = conn.recv(4096)
		if data == 'quit':
			break
		print data
	conn.send('Goodbye')
	sock.shutdown('SHUT_RDWR')
