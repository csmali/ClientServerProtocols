from socket import *
serverPort=12000
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print "Server is ready to receive"
while 1:
	message,clientAddress = serverSocket.recvfrom(2048)
	print "Message is received " + message;
	modifiedMessage = message.upper()
	serverSocket.sendto(modifiedMessage,clientAddress)
