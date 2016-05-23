import sys
import os
import logging
import time
import re

from Tkinter import Tcl


class tcl_shell(object):
	'''
	'''

	def __init__(self):
		print 'try open an handle for tcl_shell'

		try:
			self.env_handle = subprocess.Popen('tclsh',                  shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE                 )
			#                                          |                        |                         |                      |    
			#                                         app                      env                     input pipline          output pipline


		except Exception:
			print 'tcl_shell init error'







		'''
		try:
			self.env_handle.stdin.write('source '+script_pwd)

		except Exception:
			print 'enter cmdline environment error'


