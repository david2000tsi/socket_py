import signal
import sys

class Signal:

	def sig_hdl(signal, fnc):
		print(' [CTRL+C]')
		exit(0)

	def add_signal():
		signal.signal(signal.SIGINT, Signal.sig_hdl)
		return
