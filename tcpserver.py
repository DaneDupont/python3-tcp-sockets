#a simple tcp-server listening on port 1212, preforms a message check and formats a response. 
import socket

expectedMSG = "Hello World (request page)"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Bind socket to localhost
hostport = ("localhost", 1212)
s.bind(hostport)
#Launch server socket listener
s.listen(5)
print("Server has been launched.")
while True:
	#Accept connections
	clientsocket,address = s.accept()
	print ("Connection from", address)
	msg = clientsocket.recv(1024).decode()
	print ("Received: ", msg)
	if msg == expectedMSG:
		print("Message authenticated... returning html response")
		clientsocket.send("TCP Hello World".encode())
	clientsocket.close()
