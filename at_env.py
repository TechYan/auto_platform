import time
import threading
import logging
import time
import subprocess
import os
import re

from Tkinter import Tcl

from card_20p200 import *
	


#---------------------------re expression-----------------------------#
re_card_opt = re.compile(r'([0-9a-zA-Z]+)\s+slot\s+([0-9]+)')
re_finish   = re.compile(r'finish')
#---------------------------------------------------------------------#


class at_env(object):
	'''
	at_env
	'''
	def __init__(self):
		print 'at_env init...'
		self.slot = {}
			


	def default_set(self):
		print 'do some thing...default_set'

	def card_plugin(self, card_type, slot_number):
		if self.slot.get(slot_number) != None:
			print 'below card is already on this slot'+str(slot_number)
			print self.slot[slot_number]
		elif card_type == '20p200':
			self.slot[slot_number] = card_20p200()
			#because class card_20p200 has default slot_number,
			#you should change it here...
			self.slot[slot_number].set_slot_num(slot_number)
		elif card_type == '1ud200':
			print '1ud200 do something here...'
			self.slot[slot_number] =None
		else:
			print '>error you just plugin an unsupported card, please check!...'



	def card_plugout(self, slot_number):
		if self.slot[slot_number] == None:
			print 'there is no card on slot'+str(slot_number)
		else:
			print 'remove the card on slot'+str(slot_number)
			self.slot.pop(slot_number)

	def get_handle(self, slot_number):
		return self.slot[slot_number]

	def mannual_mode(self):
		#env set
		print '>please set your test env...'
		print '>eg: 20p200 slot 2'
		print '>when finished, please input:  $finish'
		while True:
			raw_cmd = raw_input('>>>cmd is:')

			opt_match = re.search(re_card_opt, raw_cmd)
			if opt_match != None:
				self.card_plugin(opt_match.group(1), opt_match.group(2))
				continue
			finish_match = re.search(re_finish, raw_cmd)
			if finish_match != None:
				print '>>>finish env config!'
				break
		print 'please '


def main():
	tmp = at_env()
	tmp.card_plugin('20p200', 2)
	tmp.card_plugin('20p200', 2)
	tmp.card_plugin('1ud200', 3)
	tmp.card_plugin('iamnotcard', 4)
	tmp.card_plugout(2)

	tmp.mannual_mode()


if __name__ == '__main__':
	main()


