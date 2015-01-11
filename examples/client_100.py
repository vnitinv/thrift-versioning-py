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
print "Starting python client version 1.0.0..."

try:
  acc = Account(234,'nitinkr','kgg')
  print 'Updating account ', acc
  client.update(acc)
  # 100 version allow resetting account with same id 234
  acc = Account(234,'hacker','pk')
  print 'Updating account ', acc
  client.update(acc)
except Thrift.TException, tx:
  print "%s" % (tx.message)

try:
  print '\nAccount lookup '
  print client.lookup(234, Mode.ADMIN, 1)
  #to get exception as in 100 version
  print client.lookup(235, 4, 1)
except InvalidAccountException as ex:
  print "Got exception while lookup: %s" % (ex.message)
#generic exception for 101 server as there for wrong id 235 we have removed exception
except Thrift.TException, tx:
  print "%s" % (tx.message)

transport.close()