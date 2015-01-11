#!/usr/bin/env python

from thrift_version import add_sys_path
add_sys_path(__file__)

import re

from interfaces import InterfacesService
from interfaces.ttypes import *
from interfaces.constants import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

   
class InterfaceServiceHandler:

    def __init__(self):
        self.interfaces = {}
    # Interface Services
    def V4InterfaceAdd(self, if_name, unit, v4_prefix, v4_prefix_len):
        print ('V4InterfaceAdd', if_name, unit, v4_prefix, v4_prefix_len)
        if not re.match(r'\w{2}-\d/\d/\d',if_name):
            raise InvalidInterfaceException('Check interface name')
        if if_name in self.interfaces:
            self.interfaces[if_name].append((unit, v4_prefix, v4_prefix_len))
        else:
            self.interfaces[if_name]=[(unit, v4_prefix, v4_prefix_len)]
        return RetStatus(100, 'added')

    def V4InterfaceDelete(self, if_name, unit, v4_prefix, v4_prefix_len):
        print ('V4InterfaceDelete', if_name, unit, v4_prefix, v4_prefix_len)
        if if_name in self.interfaces:
            del self.interfaces[if_name]
            return True
        else:
            return False

    def InterfaceExists(self, if_name):
        if if_name in self.interfaces:
            print 'Interface %s exists'%if_name
        else:
            print 'Interface %s does not exists'%if_name

handler = InterfaceServiceHandler()
processor = InterfacesService.Processor(handler)
transport = TSocket.TServerSocket(port=9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print "Starting python server version 1.0.0..."
server.serve()
print "done!"
