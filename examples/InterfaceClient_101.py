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

print "Starting python client version 1.0.1..."

try:
    print '#'*60
    result = intf.V4InterfaceAdd('ge-0/0/45', 0, '10.209.11.176', 24)
    print 'Invoked V4InterfaceAdd \nreturn = ', result
    # V4InterfaceDelete will start returning struct RetStatus from 1.0.1
    result = intf.V4InterfaceDelete('ge-0/0/45', 0, '10.209.11.176', 24)
    print 'Invoked V4InterfaceDelete \nreturn = ', result
except Exception as tx:
    print '%s' % (tx.message)

try:
    print '#'*60
    # wrong interface which never got added
    result = intf.V4InterfaceDelete('ge-0/0/46', 0, '10.209.11.176', 24)
    print 'Invoked V4InterfaceDelete \nreturn = ', result
except Exception as tx:
    print '%s' % (tx.message)

# 100 used to throw specific exception, 101 wont throw that
try:
    print '#'*60
    result = intf.V4InterfaceAdd('text', 0, '10.209.11.176', 24)
    print 'Invoked V4InterfaceAdd \nreturn = ', result
except Exception as tx:
    print '%s' % (tx.message)

# V4InterfaceEdit throws specific error in 101
try:
    print '#'*60
    # invalid interface name which get validated on server
    result = intf.V4InterfaceAdd('ge-0/0/45', 0, '10.209.11.176', 24)
    print 'Invoked V4InterfaceAdd \nreturn = ', result
    result = intf.V4InterfaceEdit('ge-0/0/45', 0, '10.0.11.176', 72)
    print 'Invoked V4InterfaceEdit \nreturn = ', result
    result = intf.V4InterfaceEdit('ge-0/1/45', 0, '10.0.11.176', 72)
    print 'Invoked V4InterfaceEdit \nreturn = ', result
except InvalidInterfaceException as tx:
    print '%s' % (tx.message)
# need to handle genric exception as otherwise it will break with 100 server
except Exception as tx:
    print '%s' % (tx.message)

try:
    print '#'*60
    # void return type function on which 1.0.1 will throw exception
    obj = RetStatus(0,'input', 'testing')
    result =  intf.InterfaceExists('ge-0/0/45', obj)
    print 'Invoked InterfaceExists \nreturn = ', result
except Exception as tx:
    print '%s' % (tx.message)