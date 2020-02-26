import sys
import os
from sys import platform

class Bash:

	def new_line():
		print('> ', end = '')
		return

	def help():
		print('Usage:')
		print('> ? - to show help')
		print('> os - to show native os')
		print('> \\c - to clear screen')
		print('> \\q - to quit bash')
		Bash.new_line();
		return

	def get_platform():
		return str(platform)

	def print_platform():
		return print(Bash.get_platform())

	def cmd_clear():
		if('linux' in Bash.get_platform()):
			return 'clear'
		return 'cls'

	def run():
		print('Python bash console started:')
		Bash.help();

		while True:
			choise = input()
			custom_new_line = False

			if(choise == '?'):
				Bash.help();

			if(choise == 'os'):
				Bash.print_platform();
				custom_new_line = True

			if(choise == '\\c'):
				os.system(Bash.cmd_clear())
				custom_new_line = True

			if(choise == ''):
				custom_new_line = True

			if(choise == '\\q'):
				break

			if(custom_new_line):
				Bash.new_line();

		return

def main():
	Bash.run()
	return

if __name__ == '__main__':
	main()
