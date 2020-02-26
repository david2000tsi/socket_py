import os.path
from os import path
from msg_util import MsgUtil

class FileUtil:

	# Create log of all messages.
	def client_log(filename, msg):
		file_status = ''
		open_mode = 'w'
		if(path.exists(filename)):
			file_status = 'existing '
			open_mode = 'a'
		
		file = open(filename, open_mode)
		MsgUtil.print_msg('LOG: [' + str(msg) + ']' + ' (saving to ' + str(file_status) + 'file)')

		file.write(msg)
		file.write('\n')
		file.close()
		return
