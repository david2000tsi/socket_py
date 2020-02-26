import sys
sys.path.append('./utils')

import socket
from msg_util import MsgUtil
from constants import Constants

class SocketSrv:

	def __init__(self):
		return

	# Create server socket.
	def create():
		tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		srv = (Constants.HOST, Constants.PORT)

		tcp.bind(srv)
		tcp.listen(Constants.MAX_CONN_SERVER)

		while True:
			con, client = tcp.accept()
			MsgUtil.print_msg('Client: [' + str(client) + '] connected')

			while True:
				msg = con.recv(Constants.MAX_BYTES_RECV_SRV)
				if not msg:
					break

				if Constants.CLOSE_SOCK_KW in msg.decode():
					break

				MsgUtil.print_msg('Client: [' + str(client) + '] Msg: [' + msg.decode() + ']')

			MsgUtil.print_msg('Closing connection')
			con.close()
		return

def main():
	SocketSrv.create()
	return

if __name__ == '__main__':
	main()
