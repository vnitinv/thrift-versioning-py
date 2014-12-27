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

  	def lookup(self,mode, id, active, name='*'):
		print 'Inside lookup: ', 'mode:', mode, 'id:', id, 'active:', active, 'name:', name
		if active and id in self.accounts:
			return AccountID(id , self.accounts[id][0], self.accounts[id][1])
		else:
			print ('account does not exists with given id %d'%id)

	def update(self, account):
		print 'Update account: ', account
		if account.id in self.accounts:
			raise InvalidAccountException('Account already exists')
		# should ignore city argument coming from older clients
		self.accounts[account.id]=(account.name, account.age)
	  	print self.accounts
		# Account object returned from 101 version
		return AccountID(account.id, account.name, account.age)
	
handler = AccountsHandler()
processor = Accounts.Processor(handler)
transport = TSocket.TServerSocket(port=9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print "Starting python server version 1.1.0..."
server.serve()
print "done!"
