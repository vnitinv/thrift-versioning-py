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
    acc = AccountID(234, 'nitinkr', 25)
    print 'Updating account ', acc
    # we are expecting Account struct as response but 100 wont sent anything
    #  client.update(acc)
except Thrift.TException, tx:
    print "Genric Exception: %s" % (tx.message)

try:
    # 101 version does not allow resetting account with same id 234
    acc = AccountID(234, 'hacker', 25)
    print 'Updating account ', acc
    client.update(acc)
except InvalidAccountException as ex:
    print "InvalidAccountException: %s" % (ex.message)
except Thrift.TException, tx:
    print "Genric Exception: %s" % (tx.message)

try:
    print '\nAccount lookup '
    print client.lookup(id=234, mode=Mode.ADMIN, name='hacker')
    # As parameter position got changes, to call with key
    x = client.lookup(Mode.ADMIN, 234, 'hacker')
    # To show even when Account struct name got changed to AccountID, fn return wont be impacted
    print 'id: ', x.id, 'name: ', x.name
    # to get specific exception as in 100 version
    client.lookup(id=235, mode=4, name='pk')

# generic exception for 101 server as there for wrong id 235 we have removed exception
except Thrift.TException, tx:
    print "Genric Exception: %s" % (tx.message)

# New functions added in 1.1.0
try:
    print '\nAccount credit'
    print client.credit(234, 410)
    print 'Credit balance of 234: ', client.credit_balance(234)
    # -ve testing
    print client.credit(235, 410)
    print 'Credit balance of 235: ', client.credit_balance(235)
except Thrift.TException, tx:
    print "Genric Exception: %s" % (tx.message)

transport.close()
