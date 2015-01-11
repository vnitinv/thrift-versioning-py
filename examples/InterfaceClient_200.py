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

try:
    print '#'*60
    # parameter postion got changes, hence calling with key/value will keep consistency
    result = intf.V4InterfaceAdd(if_name='ge-0/0/45', unit=0, prefix='10.209.11.176', size=36)
    print 'Invoked V4InterfaceAdd \nreturn = ', result

    # As parameter position got changes following the new order with keys only
    result = intf.V4InterfaceAdd('ge-0/0/45', '10.209.11.176', 0, 24)
    print 'Invoked V4InterfaceAdd \nreturn = ', result

    result = intf.V4InterfaceRemove('ge-0/0/45', 0, '10.209.11.176', 24)
    print 'Invoked V4InterfaceRemove \nreturn = ', result
except Exception as tx:
    print '%s' % (tx.message)

# V4InterfaceDelete throws specific error in 101
try:
    print '#'*60
    # wrong interface which never got added
    result = intf.V4InterfaceRemove('ge-0/0/46', 0, '10.209.11.176', 24)
    print 'Invoked V4InterfaceRemove \nreturn = ', result
except InvalidInterfaceException as tx:
    print '%s' % (tx.message)

# 100 used to throw specific exception, 101 wont throw that
try:
    print '#'*60
    result = intf.V4InterfaceAdd('text', '10.209.11.176', 0, 24)
    print 'Invoked V4InterfaceAdd \nreturn = ', result
except Exception as tx:
    print '%s' % (tx.message)

try:
    print '#'*60
    result = intf.V4InterfaceAdd('ge-0/0/45', '10.209.11.176', 0, 24)
    print 'Invoked V4InterfaceAdd \nreturn = ', result
    result = intf.V4InterfaceAdd('ge-0/0/45', '71.2.34.34', 1, 96)
    print 'Invoked V4InterfaceAdd \nreturn = ', result
    result = intf.InterfaceGet(0)
    print 'Invoked InterfaceGet \nreturn = ', result
    result = intf.InterfaceGet(1)
    print 'Invoked InterfaceGet \nreturn = ', result
    # function removed in 2.0.0
    # result = intf.InterfaceStatsGet('ge-0/0/45')
    # print 'Invoked InterfaceStatsGet \nreturn = ', result
except Exception as tx:
    print '%s' % (tx.message)