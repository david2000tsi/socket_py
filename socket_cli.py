import socket
from file_util import client_log

HOST = '127.0.0.1'
PORT = 8000
CLOSE_SOCK = 'quit'
LOG_FILE = 'logs/socket_cli.log'

# Create socket.
def soket_cli():
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	dest = (HOST, PORT)

	print ('Trying to connect in socket...\n')
	tcp.connect(dest)

	while True:
		msg = input('Write a message please\n')
		client_log(LOG_FILE, msg)
		tcp.send(msg.encode())
		print ('Sending: [', msg, ']')

		if CLOSE_SOCK in msg:
			break

	print ('Closing connection\n')
	tcp.close()
	return

def main():
	soket_cli()
	return

if __name__ == '__main__':
	main()
