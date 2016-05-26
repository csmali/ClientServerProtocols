from socket import *
serverName = 'localhost'
serverPort=12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message=raw_input('Inout lowercase sentece:')
clientSocket.sendto(message,(serverName,serverPort))
modifiedMessage,serverAdress=clientSocket.recvfrom(2048)
print modifiedMessage
clientSocket.close()
