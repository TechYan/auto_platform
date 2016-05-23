
import time
import threading
import logging
import time
import subprocess
import os
import re

from Tkinter import Tcl


from tcl_shell import*

#-------------------global parameter--------------------#
TCL_20P200_RUN_PATH = '/home/common_test/falcon_test/test_20P200/20P200_shelf_test/remote_test_target/test_main.tcl'

#-------------------re expression-----------------------#
re_dbgCut_wrl = re.compile(r'\(flts 0 otumach 1 [0-9]\)  \"drvdbg kitewrite__(0x[0-9a-zA_Z]{8})_(0x[0-9a-zA-Z]+)_2\"')
re_dbgCut_rdl = re.compile(r'kite read reg (0x[0-9]+) on bar [0-9]+: data = (0x[0-9a-zA-Z]+)')



class card_20p200_tcl_env(tcl_shell):
	'''
	card_20p200_tcl_env
	'''

	def __init__(self):
		super(card_20p200_tcl_env, self).__init__()
		print 'init card_20p200_tcl_env val'
		self.script_pwd = ''
		self.slot_num   = 2

	def config_20p200_tcl_env(self, slot_num = '2'):
		print self.debug_val
		self.env_handle.stdin.write('set slot_num' +slot_num+'\n')
		self.env_handle.stdin.write('source '+TCL_20P200_RUN_PATH+'\n')

	def wrl_reg(self, ADDR = '0x00000000', DATA = '0x0'):
		super(card_20p200_tcl_env).env_handle.stdin.write('mm --wrl' +ADDR+' '+DATA+'\n')
		try:
			while True:
				raw_print = self.env_handle.stdout.readline()
				re_match = re.search(re_dbgCut_wrl, raw_print)

				if re_match != None and re_match.group(1) == ADDR:
					break
		except Exception:
			print 'catch wrl raw_print error'

	def rdl_reg(self, ADDR = '0x00000000'):
		self.env_handle.stdin.write('mm --rdl' +ADDR+' '+DATA+'\n')
		try:
			while True:
				raw_print = self.env_handle.stdout.readline()
				re_match = re.search(re_dbgCut_rdl, raw_print)

				if re_match != None and eval(re_match.group(1)) == eval(ADDR):
					rdl_val = re_match.group(2)
					break
		except Exception:
			print 'catch rdl raw_print error'
		return rdl_val






