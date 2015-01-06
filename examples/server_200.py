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
		self.balance = {}

  	def lookup(self, mode, id, name):
		print 'Inside lookup: ', 'mode:', mode, 'id:', id, 'name:', name
		if id in self.accounts:
			if name=='*':	#this will help older client
			    return AccountID(id , self.accounts[id][0], self.accounts[id][1])
			elif self.accounts[id][0]==name:
				return AccountID(id , self.accounts[id][0], self.accounts[id][1])
			else:
				print ('account does not exists with given id %d and name %s'%(id, name))
		else:
			print ('account does not exists with given id %d'%id)

	def update_account(self, account):
		print 'Update account: ', account
		if account.id in self.accounts:
			raise InvalidAccountException('Account already exists')
		# should ignore city argument coming from older clients
		self.accounts[account.id]=(account.name, account.age)
	  	print self.accounts
		# Account object returned from 101 version
		return AccountID(account.id, account.name, account.age)

	#new functions added
	def credit(self, id, amount):
		if id in self.accounts:
			if id not in self.balance:
				self.balance.setdefault(id, amount)
			else:
				self.balance[id]+=amount
			print 'Credit balance of %d: %d'%(id, self.balance[id])
			return True
		else:
			print 'Given id %d dont have account'%id
			return False

	def debit(self, id, amount):
		if id in self.accounts or id in self.balance:
			if self.balance[id]>=amount:
				self.balance[id]-=amount
				print 'Credit balance of %d: %d'%(id, self.balance[id])
				return True
			else:
				print 'You do not have sufficient balance in your account'
				return False
		else:
			print 'Given id %d dont have account or balance'%id
			return False
	
handler = AccountsHandler()
processor = Accounts.Processor(handler)
transport = TSocket.TServerSocket(port=9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print "Starting python server version 2.0.0..."
server.serve()
print "done!"
