import socket

HOST = '127.0.0.1'
PORT = 8000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)

print ('Trying to connect in socket...\n')
tcp.connect(dest)

msg = input('Write a message please\n')
while len(msg) > 0:
	tcp.send(msg.encode())
	print ('Sending: [', msg, ']')
	msg = input('Write a new message please\n')

print ('Closing connection\n')
tcp.close()
