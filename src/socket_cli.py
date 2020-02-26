import sys
sys.path.append('./utils')

import socket
from file_util import FileUtil
from msg_util import MsgUtil
from constants import Constants

class SocketCli:

	def __init__(self):
		return

	# Create client socket.
	def create():
		tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		dest = (Constants.HOST, Constants.PORT)

		MsgUtil.print_msg('Trying to connect in socket...')
		tcp.connect(dest)
		MsgUtil.print_msg('Use \'' + Constants.CLOSE_SOCK_KW + '\' to close socket')

		while True:
			msg = input('Write a message please\n')
			FileUtil.client_log(Constants.CLIENT_LOG_FILENAME, msg)
			tcp.send(msg.encode())
			MsgUtil.print_msg('Sending: [' + str(msg) + ']')

			if Constants.CLOSE_SOCK_KW in msg:
				break

		MsgUtil.print_msg('Closing connection')
		tcp.close()
		return

def main():
	SocketCli.create()
	return

if __name__ == '__main__':
	main()
