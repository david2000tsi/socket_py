import signal
import sys

class Signal:

	# Handle signals from user.
	def sig_hdl(signal, fnc):
		print(' [CTRL+C]')
		exit(0)

	# Enable signal handling.
	def add_signal():
		signal.signal(signal.SIGINT, Signal.sig_hdl)
		return
