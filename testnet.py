#!/opt/local/bin/python

import socket               # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
c, addr = s.accept()        # Establish connection with client.
print 'Got connection from', addr
while 1:
	c.send('Thank you for connecting!')
	data = c.recv(4096) #receive data from client
	if not data: break
	print data
c.close()           # Close the connection
