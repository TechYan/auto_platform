import sys
import os
import logging
import time
import re

from telnetlib import *


#ec
ec_ip_addr  = '135.252.213.141'
ec_usr_name = 'root'
ec_pwd      = 'ALu12#' 


login_str        = 'login:'
pwd_str          = 'password:'
return_value_str = 'root@8EC2-81-1-ACT:'


class telnet_env(object):
	'''
	telnet...
	'''

	def __init__(self):
		print 'try open an handle for one telnet'

		try:
			self.username = ec_usr_name+'\n'
			self.password = ec_pwd+'\n'

			self.tn = Telnet(ec_ip_addr)

			print '>wait 8s and python will auto input username and password...'
			#time.sleep(6)

			#self.username = self.username.encode('utf-8')
			print self.tn.read_until(login_str)
			self.tn.write(self.username)
			#time.sleep(2)
			#self.password = self.password.encode('utf-8')
			print self.tn.read_until(pwd_str, 10)
			self.tn.write(self.password)
			print self.tn.read_until(return_value_str, 10)

		except Exception:
			print 'unable to set the telnet env'

	def tn_send(self, cmd = ''):
		cmd = cmd +'\n'
		cmd = cmd.encode('utf-8')
		try:
			self.tn.write(cmd)
                        time.sleep(0.1)
			#try read out all printed info
			raw_print = self.tn.read_very_eager()
			#raw_print = raw_print + self.tn.read_very_eager()
			#raw_print = raw_print + self.tn.read_very_eager()
                        print raw_print
			return raw_print		
		except Exception:
			print '>error: when use tn_send...(in class telnet_env)'


def main():
	tmp = telnet_env()
	tmp.tn_send('ls')
	tmp.tn_send('pwd')

if __name__ == '__main__':
	main()