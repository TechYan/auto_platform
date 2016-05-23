import sys
import os
import logging
import time
import re

from telnetlib import *
from card_20p200 import *
from build_phase import *


#---------------------------re expression--------------------------------
re_config_cmd = re.compile(r'mm --(wrl|rdl)\s+(0[xX][0-9a-zA-Z]+)\s*(0[xX][0-9a-zA-Z]+)*')

re_config_file = re.compile(r'Name:\s*([0-9a-zA-Z]+)\s+Conf_FILE:\s*(\S*)')
#------------------------------------------------------------------------

class config_phase(object):
	'''
	config at env
	'''

	def __init__(self):
		self.config_list = []


	def config_file_proc(self, file_name= '', tm_handle = None):
		try:
			print '>debug: '+file_name
			f = open(file_name, 'r')
			while True:
				raw_str = f.readline()
				raw_match = re.search(re_config_cmd, raw_str)
				if raw_str == '':
					break
				elif re.search(re_config_cmd, raw_str) != None:
					raw_match = re.search(re_config_cmd, raw_str)
					if raw_match.group(1) == 'rdl':
						tm_handle.reg_rdl(eval(raw_match.group(2)))
					elif raw_match.group(1) == 'wrl':
						tm_handle.reg_wrl(address = eval(raw_match.group(2)), data_val = eval(raw_match.group(3)))
		except IOError:
			print '>error: can not find your config file! please check...'


	def sel_config_phase_file(self, card_name = 'somecard', build_phase_handle = None, sel_file_name = ''):
		if build_phase_handle.dev_handle[card_name] == None:
			print '>error: the card you wanna config is not been set to at_env yet!'
			print '>error: try to check your build_phase and your build_config_file.cfg'
			return
		else:
			self.config_file_proc(file_name = sel_file_name, tm_handle = build_phase_handle.dev_handle[card_name])


	def sel_config_phase_file_proc(self, file_name = ''):
		#each time sel one config file, just refresh the buffer
		print '>debug: into sel_config_phase_file_proc'
		self.config_list = []

		try:
			f = open(file_name, 'r')
			while True:
				raw_str = f.readline()
				print raw_str
				if raw_str == '':
					break
				elif re.search(re_config_file, raw_str) != None:
					raw_match = re.search(re_config_file, raw_str)
					dev_config_dict = {'Name' : raw_match.group(1),\
									   'Path' : raw_match.group(2)}
					self.config_list.append(dev_config_dict)

		except Exception:
			print '>error: try get config phase file, but can not get!...'



	def config_phase_proc(self, build_handle = [], config_file_path = ''):
		print build_handle
		print config_file_path
		self.sel_config_phase_file_proc(file_name = config_file_path)
		print self.config_list
		
		for item in self.config_list:
			print item
			self.sel_config_phase_file(item['Name'], build_handle, sel_file_name = item['Path'])
			print '>info: finish config card'
		


def main():

	#tmp_handle = card_20p200()
	#tmp_handle_1 = card_20p200()
	cf = config_phase()
	bf = build_phase()
	bf.sel_build_phase_file('./env_config_profile/tb3/build_config_file.cfg')
	bf.build_phase_proc()
	#cf.config_file_proc('/home/yshuai/test_work/python_test/auto_platform/env_config_profile/tb3/tb3_testcase1003_1.ip0.slot1.linux', tmp_handle)

	#tmp_hd = dict(W = tmp_handle)
	#tmp_hd_1 = dict(P = tmp_handle_1)
	#tmp_handle_list = []
	#tmp_handle_list.append(tmp_hd)
	#print tmp_hd
	#tmp_handle_list.append(tmp_hd_1)
	
	
	#print tmp_hd
	
	print bf.dev_handle
	cf.config_phase_proc(build_handle = bf, config_file_path = '/home/yshuai/test_work/python_test/auto_platform/env_config_profile/tb3/initial_configuration.cfg')


if __name__ == '__main__':
	main()
