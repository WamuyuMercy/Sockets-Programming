import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
	clientsocket, address = s.accept()
	print("connection established!")
	data = clientsocket.recv(1024).decode()
	print("Message from " + str(data))
	clientsocket.send(bytes("message received", "utf-8"))

s.close()