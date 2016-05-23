import time
import threading
import logging
import time
import subprocess
import os
import re

from Tkinter import Tcl

from dbgCut import *

#--------------------parameter---------------------#
reg_wrl_re_20p200 = re.compile(r'\(flts 0 otumach 1 [0-9]\)  \"drvdbg kitewrite__(0x[0-9a-zA_Z]{8})_(0x[0-9a-zA-Z]+)_2\"')
reg_rdl_re_20p200 = re.compile(r'kite read reg (0x[0-9]+) on bar [0-9]+: data = (0x[0-9a-zA-Z]+)')


class card_20p200(dbgCut):
	'''
	card 20p200 get access via telnet
	'''

	def __init__(self):
		super(card_20p200, self).__init__()
		print 'init card_20p200_telnet_env val'
		self.slot_num = 2

	def set_slot_num(self, SLOTID = 2):
		self.slot_num = SLOTID

	def reg_rdl(self, address = 0x0):
		raw_data = self.dbgCut_rd_cmd(slotID = self.slot_num, addr = address, bar = self.slot_num)
		raw_match = re.search(reg_rdl_re_20p200, raw_data)


		if raw_match != None and eval(raw_match.group(1)) == eval(str(address)):
			rdl_val = raw_match.group(2)
			return rdl_val
		else:
			print ">error: can not get valid data via reg_rdl"

	def reg_wrl(self, address = 0x0, data_val = 0x0):
		raw_data = self.dbgCut_wr_cmd(slotID = self.slot_num, addr = address, data = data_val)
		raw_match = re.search(reg_wrl_re_20p200, raw_data)

		if raw_match != None and eval(raw_match.group(2)) == eval(str(address)):
			wrl_val = raw_match.group(3)
			return wrl_val
		else:
			print ">error: can not get valid data via reg_wrl"


def main():
	tmp = card_20p200()
	print tmp.reg_rdl(address = 0x0)


if __name__ == '__main__':
	main()



