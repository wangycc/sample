#!/bin/python
import socket
import SocketServer
class MyTCPHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		print "got a connection from",self.client_address[0]
		while True:
			self.data = self.request.recv(1024).strip()
			if not self.data:
				print "Client is disconnected...",self.client_address[0]
				break
			print self.data
			if self.data.split()[0] == 'put':
				print "Going to receive File",self.data.split()[1]
				f = file('recv/%s' %self.data.split()[1],'wb')
				self.request.send("ReadyToReceiveFile")
				data = 'df'
				while 1:
					data = self.request.recv(4096)
					if data == "FileSendDone":
						print "Transfer is done.."
						break
					print '##' * 20
					f.write(data)
				f.close()
			self.request.sendall(self.data.upper())
if __name__ == "__main__":
	HOST,PORT = 'localhost',9999
	server = SocketServer.ThreadingTCPServer((HOST,PORT),MyTCPHandler)
	server.serve_forever()
