import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))
str = input("Enter your name:")

while True:
	s.send(str.encode())
	msg = s.recv(1024)
	print("Message from server: " + msg.decode("utf-8"))

s.close()