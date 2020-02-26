from datetime_util import DatetimeUtil

class MsgUtil:

	# Mount formatted message with datetime.
	def mk_msg(msg):
		return str('(' + DatetimeUtil.get_datetime_str() + ') [' + str(msg) + ']')

	# Print formatted message.
	def print_msg(msg):
		print(MsgUtil.mk_msg(msg))
		return
