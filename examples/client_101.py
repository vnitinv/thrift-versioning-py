from thrift_version import add_sys_path
add_sys_path(__file__)


from accounts import Accounts
from accounts.ttypes import *
from accounts.constants import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

transport = TSocket.TSocket('localhost', 9090)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = Accounts.Client(protocol)

transport.open()

try:
  acc = Account(234, 'nitinkr', 'kgg', 25)
  print 'Updating account ', acc
  # we are expecting Account struct as response but 100 wont sent anything
  client.update(acc)
except Thrift.TException, tx:
  print "%s" % (tx.message)

try:
  # 101 version does not allow resetting account with same id 234
  acc = Account(234, 'hacker', 'pk', 25)
  print 'Updating account ', acc
  client.update(acc)
except InvalidAccountException as ex:
  print "InvalidAccountException: %s" % (ex.message)
except Thrift.TException, tx:
  print "Genric Exception: %s" % (tx.message)

try:
  print '\nAccount lookup '
  print client.lookup(234, Mode.ADMIN, 1)
  #to get specific exception as in 100 version
  print client.lookup(235, 4, 1)
except InvalidAccountException as ex:
  print "Got exception while lookup: %s" % (ex.message)
# generic exception for 101 server as there for wrong id 235 we have removed exception
except Thrift.TException, tx:
  print "Genric Exception: %s" % (tx.message)

transport.close()
