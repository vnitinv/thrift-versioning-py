#!/usr/bin/env python

from thrift_version import add_sys_path
add_sys_path(__file__)

from accounts import Accounts 
from accounts.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class AccountsHandler:
  	def __init__(self):
		self.accounts = {}

  	def lookup(self,id, mode, active):
		print 'Inside lookup'
		print id, mode, active
		if active and id in self.accounts:
			return Account(id , self.accounts[id][0], self.accounts[id][1])
		else:
			raise InvalidAccountException('account does not exists')

	def update(self,account):
		print 'Update account'
		self.accounts[account.id]=(account.name, account.city)
	  	print self.accounts
	
handler = AccountsHandler()
processor = Accounts.Processor(handler)
transport = TSocket.TServerSocket(port=9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print "Starting python server..."
server.serve()
print "done!"
