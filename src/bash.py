import sys
import os
from sys import platform
from cryptography.fernet import Fernet

class Cryptography:

	key = Fernet.generate_key()

	def encrypt(txt):
		cipher = Fernet(Cryptography.key)
		txt_byte = str(txt).encode()
		return (cipher.encrypt(txt_byte)).decode()

	def decrypt(chp_txt):
		cipher = Fernet(Cryptography.key)
		txt_byte = str(chp_txt).encode()
		return (cipher.decrypt(txt_byte)).decode()

class Bash:

	def new_line():
		print('> ', end = '')
		return

	def help():
		print('Usage:')
		print('> ? - to show help')
		print('> os - to show native os')
		print('> enc <msg> - to encrypt msg')
		print('> dec <msg> - to decrypt msg')
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
			valid = False

			if(choise == '?'):
				Bash.help();
				valid = True

			if(choise == 'os'):
				Bash.print_platform();
				custom_new_line = True
				valid = True

			if(choise.find('enc ') == 0):
				txt = choise.replace('enc ', '')
				print(Cryptography.encrypt(txt))
				custom_new_line = True
				valid = True

			if(choise.find('dec ') == 0):
				txt = choise.replace('dec ', '')
				print(Cryptography.decrypt(txt))
				custom_new_line = True
				valid = True

			if(choise == '\\c'):
				os.system(Bash.cmd_clear())
				custom_new_line = True
				valid = True

			if(choise == ''):
				custom_new_line = True
				valid = True

			if(choise == '\\q'):
				break

			if(valid == False):
				print('Invalid option!')
				custom_new_line = True

			if(custom_new_line):
				Bash.new_line();

		return

def main():
	Bash.run()
	return

if __name__ == '__main__':
	main()
