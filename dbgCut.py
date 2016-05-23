from telnet_env import *


#---------parameter------------
dbgCut_prompt = 'dbgCut>'


class dbgCut(telnet_env):
	"""docstring for dbgCut"""
	def __init__(self):
		print 'enter telent_env class and create an handle for one telnet'
		super(dbgCut, self).__init__()


		self.app_path = '/pureNeApp/EC/dbgCut'
		try:
			print 'py print >@ try enter dbgCut app on ec'
			print self.tn_send(self.app_path)

			#self.tn_send.read_until(dbgCut_prompt, 10)
			print 'pyt print >@ enter dbgCut app success'

		except Exception:
			print 'can not get access to dbgCut app on EC'


#command format:
#!dbgCutThru (FLTS 0 OTUMACH 1 slotID) "drvdbg kiteread__<addr>_<bar>"
#!dbgCutThru (FLTS 0 OTUMACH 1 slotID) "drvdbg kitewrite__<addr>_<data>_<bar>"

	def dbgCut_wr_cmd(self, slotID = 2, addr = 0x0, data = 0x0, bar = 2):
		dbgCut_command = '!dbgCutThru (FLTS 0 OTUMACH 1 '+str(slotID)+') "drvdbg kitewrite_'+str(hex(addr))+'_'+str(hex(data))+'_'+str(bar)+'"'

		raw_data = self.tn_send(dbgCut_command)
		return raw_data


	def dbgCut_rd_cmd(self, slotID = 2, addr = 0x0, bar = 2):
		dbgCut_command = '!dbgCutThru (FLTS 0 OTUMACH 1 '+str(slotID)+') "drvdbg kiteread__'+str(hex(addr))+'_'+str(hex(bar))+'"'

		raw_data = self.tn_send(dbgCut_command)
		return raw_data



def main():
	tmp = dbgCut()
	tmp.dbgCut_rd_cmd(slotID=2, addr = 0x0,bar = 2)


if __name__ == '__main__':
	main()




