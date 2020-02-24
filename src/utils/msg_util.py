from datetime_util import get_datetime_str

def mk_msg(msg):
	return str('(' + get_datetime_str() + ') [' + str(msg) + ']')

def print_msg(msg):
	print(mk_msg(msg))
	return
