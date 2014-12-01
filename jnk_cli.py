import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.3.56', 12345))
count = 0
while True:
	data = s.recv(1024)
	if data:
		if data == 'Goodbye':
			break
		count += 1
		msg = 'FOO'
		if count >= 100:
			msg = 'quit'
		print "Got {}".format(data)
		s.send(msg)
