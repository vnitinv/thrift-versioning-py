#!/usr/bin/env python
from thrift_version import add_sys_path
add_sys_path(__file__)

from interfaces import InterfacesService 
from interfaces.ttypes import *
from interfaces.constants import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

transport = TSocket.TSocket('localhost', 9090)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
intf = InterfacesService.Client(protocol)
transport.open()

print "Starting python client version 1.0.0..."

try:
    print '#'*60
    result = intf.V4InterfaceAdd('ge-0/0/45', 0, '10.209.11.176', 24)
    print 'Invoked V4InterfaceAdd \nreturn = ', result

    result = intf.V4InterfaceDelete('ge-0/0/45', 0, '10.209.11.176', 24)
    print 'Invoked V4InterfaceDelete \nreturn = ', result

    # wrong interface which never got added
    result = intf.V4InterfaceDelete('ge-0/0/46', 0, '10.209.11.176', 24)
    print 'Invoked V4InterfaceDelete \nreturn = ', result
except Exception as tx:
    print '%s' % (tx.message)

try:
    print '#'*60
    # invalid interface name which get validated on server
    result = intf.V4InterfaceAdd('text', 0, '10.209.11.176', 24)
    print 'Invoked V4InterfaceAdd \nreturn = ', result
except InvalidInterfaceException as tx:
    print '%s' % (tx.message)


print '#'*60
intf.V4InterfaceAdd('ge-0/0/45', 0, '10.209.11.176', 24)
# void return type function on which 1.0.1 will throw exception
print intf.InterfaceExists('ge-0/0/45')
# below call should ignore exception raised by 1.0.1 (only if function return type is void)
print intf.InterfaceExists('ge-0/0/47')
