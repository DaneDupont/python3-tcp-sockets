#a simple tcp-socket client connection to a localhost server. Sends a Message to specified server and displays response.
#python 3.0+
import socket

sendstring = "Hello World (request page)"
print("Messaging server...")
# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 1212))
s.send(sendstring.encode())
#wait for response from server
msg = s.recv(1024).decode()
print ("Received HTML from server:", msg)