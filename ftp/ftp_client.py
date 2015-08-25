#!/bin/python
import socket
import time
buffer = 1024
server_address = ('localhost',9999)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
	client.connect(server_address)
	while 1:
		data = raw_input('please input your transfer data:')
		if len(data) == 0:continue
		client.sendall(data)
		data1 = client.recv(buffer)
		if data1 == 'ReadyToReceiveFile':
			with file(data.split()[1]) as f:
				client.sendall(f.read())
				time.sleep(0.5)
				client.send("FileSendDone")
			
		print data1
except socket.error:
	print "server Error"
client.close()

