import socket
from file_util import client_log
from msg_util import print_msg

HOST = '127.0.0.1'
PORT = 8000
CLOSE_SOCK = '\\quit'
LOG_FILE = 'logs/socket_cli.log'

# Create socket.
def soket_cli():
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	dest = (HOST, PORT)

	print_msg('Trying to connect in socket...')
	tcp.connect(dest)
	print_msg('Use \'' + CLOSE_SOCK + '\' to close socket')

	while True:
		msg = input('Write a message please\n')
		client_log(LOG_FILE, msg)
		tcp.send(msg.encode())
		print_msg('Sending: [' + str(msg) + ']')

		if CLOSE_SOCK in msg:
			break

	print_msg('Closing connection')
	tcp.close()
	return

def main():
	soket_cli()
	return

if __name__ == '__main__':
	main()
