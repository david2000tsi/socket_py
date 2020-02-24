import os.path
from os import path

# Create log of all messages.
def client_log(filename, msg):
	file_status = ''
	open_mode = 'w'
	if(path.exists(filename)):
		file_status = 'existing '
		open_mode = 'a'
	
	file = open(filename, open_mode)
	print('LOG: [', msg, ']', ' (saving to ', file_status, 'file)')

	file.write(msg)
	file.write('\n')
	file.close()
	return
