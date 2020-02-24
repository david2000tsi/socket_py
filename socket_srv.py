import socket

HOST = '127.0.0.1'
PORT = 8000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv = (HOST, PORT)

tcp.bind(srv)
tcp.listen(1)

while True:
	con, client = tcp.accept()
	print ('Client: [', client, '] connected...\n')

	while True:
		msg = con.recv(1024)
		if not msg:
			break

		print ('Client: [', client, '] msg: [', msg, ']')

	print ('Closing connection\n')
	con.close()
