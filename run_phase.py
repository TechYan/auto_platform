import sys
import os
import logging
import time
import re

from build_phase import *
from config_phase import *

#-------------------------------re expression--------------------------
re_sel_card = re.compile(r'set\s+card\s+([0-9a-zA-Z]+)')
re_run_cmd  = re.compile(r'mm --(wrl|rdl)\s+(0[xX][0-9a-zA-Z]+)\s*(0[xX][0-9a-zA-Z]+)*')



class run_phase(object):
	'''
	run at env
	'''

	def __init__(self):
		self.run_list = []



	def run_phase_proc(self, build_handle = [], run_file_path = ''):
		print '>debug: '
		print build_handle.dev_handle
		self.run_list = []
		cur_card = ''
		f = open(run_file_path, 'r')
		while True:
			raw_str = f.readline()
			if raw_str == '':
				break
			elif re.search(re_sel_card, raw_str) != None:
				raw_match = re.search(re_sel_card, raw_str)
				print '>debug:'
				print raw_match.group(1)
				cur_card = raw_match.group(1)
				if build_handle.dev_handle[cur_card] == None:
					print '>error: please check your run phase file, the card name is not in current at environment'
					break
					
			elif re.search(re_run_cmd, raw_str) != None:
				raw_match = re.search(re_run_cmd, raw_str)
				if raw_match.group(1) == 'rdl':
					build_handle.dev_handle[cur_card].reg_rdl((eval(raw_match.group(2))))
				elif raw_match.group(1) == 'wrl':
					build_handle.dev_handle[cur_card].reg_wrl(eval(raw_match.group(2)), eval(raw_match.group(3)))



def main():
	bf  = build_phase()
	bf.sel_build_phase_file('./env_config_profile/tb3/build_config_file.cfg')
	bf.build_phase_proc()
	tmp = run_phase()
	tmp.run_phase_proc(bf, './testcase/tb3/testcase1001')


if __name__ == '__main__':
	main()


