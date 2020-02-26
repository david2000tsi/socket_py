import os.path
from os import path
from msg_util import MsgUtil

class FileUtil:

	# Create log of all messages.
	def client_log(filename, msg):
		MsgUtil.print_msg('LOG: (saving to file) [' + str(msg) + ']')
		FileUtil.write_to_file(filename, msg, True);
		return

	def write_to_file(filename, msg, insert_new_line):
		open_mode = 'w'
		if(path.exists(filename)):
			open_mode = 'a'

		file = open(filename, open_mode)
		file.write(msg)
		if(insert_new_line):
			file.write('\n')

		file.close()
		return
