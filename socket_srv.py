import socket
from msg_util import print_msg

HOST = '127.0.0.1'
PORT = 8000
CLOSE_SOCK = '\\quit'

def socket_srv():
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	srv = (HOST, PORT)

	tcp.bind(srv)
	tcp.listen(1)

	while True:
		con, client = tcp.accept()
		print_msg('Client: [' + str(client) + '] connected')

		while True:
			msg = con.recv(1024)
			if not msg:
				break

			if CLOSE_SOCK in msg.decode():
				break

			print_msg('Client: [' + str(client) + '] msg: [' + str(msg) + ']')

		print_msg('Closing connection')
		con.close()
	return

def main():
	socket_srv()
	return

if __name__ == '__main__':
	main()
