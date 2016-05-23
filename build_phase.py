import sys
import os
import logging
import time
import re

from telnetlib import *

from at_env import *

#-----------------------------re expression---------------------------------
re_config = re.compile(r'(Device):\s*([0-9a-zA-Z]+)\s+(Name):\s*([0-9a-zA-Z]+)\s+(Slot):\s*([0-9NnAa]+)\s+(Access):\s*([0-9a-zA-Z]+)\s*')
#                           |              |             |             |            |           |             |            |
#                         group1         group2        group3        group4       group5      group6        group7       group8
#---------------------------------------------------------------------------

class build_phase(at_env):
	'''
	build test env
	'''

	def __init__(self):
		super(build_phase, self).__init__()
		self.build_config_list = []

		self.dev_handle ={}


	def sel_build_phase_file(self,file_name = ''):
		'''
		this func will try open the target file for environment build,
		read out the context and store them into the build_config_list[]
		...
		'''
		try:
			f = open(file_name, 'r')
			while True:
				raw_str = f.readline()
				print raw_str
				if raw_str == '': 
					break
				elif re.search(re_config, raw_str) != None:
					raw_match = re.search(re_config,raw_str)

					#dev_key    = [group(1), group(2)]
					#name_key   = [group(3), group(4)]
					#slot_key   = [group(5), group(6)]
					#acc_key    = [group(7), group(8)]

					dev_config_dict = {'dev'   : raw_match.group(2),\
									   'name'  : raw_match.group(4),\
									   'slot'  : raw_match.group(6),\
									   'acc'   : raw_match.group(8)}

					self.build_config_list.append(dev_config_dict)

		except Exception:
			print '>error: try get build phase file, but can not get!...'

	
	def build_phase_proc(self):
		print '***********************************'
		print '*          your env is:           *'
		print self.build_config_list
		print '***********************************'		

		for item in self.build_config_list:
			if item['dev'] == '20p200' or item['dev'] == '1ud200':
				super.card_plugin(item['dev'], int(item['slot']))
				print '>info: plugin '+item['name']+' on slot:'+item['slot']+'...'

				self.dev_handle[item['name']] = super.get_handle(int(item['slot']))
				print '>info: get handle success'


def main():
	build_phase_1 = build_phase()
	build_phase_1.sel_build_phase_file('./env_config_profile/tb3/build_config_file.cfg')
	build_phase_1.build_phase_proc()
	
if __name__ == '__main__':
	main()






