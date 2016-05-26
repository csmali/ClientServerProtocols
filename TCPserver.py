from socket import *
serverPort =12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print 'The server is ready to receive'
cnt=0
while 1:
	cnt = cnt+1
	connectionSocket,addr = serverSocket.accept()
	print 'New connection is established Count %d' %cnt 
	sentence = connectionSocket.recv(1024)
	capitalizedSentence = sentence.upper()
	connectionSocket.send(capitalizedSentence)
	connectionSocket.close()
