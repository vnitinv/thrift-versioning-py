#!/usr/bin/env python

from thrift_version import add_sys_path
add_sys_path(__file__)

import re

from interfaces import InterfacesService
from interfaces.ttypes import *
from interfaces.constants import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

   
class InterfaceServiceHandler:

    def __init__(self):
        self.interfaces = {}
    # Interface Services
    def V4InterfaceAdd(self, if_name, prefix, unit, size):
        print ('V4InterfaceAdd', if_name, unit, prefix, size)
        if not re.match(r'\w{2}-\d/\d/\d',if_name):
            # RetStatus changed to ReturnStatus in 1.1.0
            return ReturnStatus(-1, 'invalid interface')
        if if_name in self.interfaces:
            self.interfaces[if_name].append((unit, prefix, size))
        else:
            self.interfaces[if_name]=[(unit, prefix, size)]
        return ReturnStatus(100, 'added')

    def V4InterfaceDelete(self, if_name, unit, v4_prefix, v4_prefix_len):
        print ('V4InterfaceDelete', if_name, unit, v4_prefix, v4_prefix_len)
        if if_name in self.interfaces:
            del self.interfaces[if_name]
            return ReturnStatus(101, 'deleted')
        else:
            raise InvalidInterfaceException('Interface %s does not exists'%if_name)

    def V4InterfaceEdit(self, if_name, unit, v4_prefix, v4_prefix_len):
        print ('V4InterfaceEdit', if_name, unit, v4_prefix, v4_prefix_len)
        if if_name in self.interfaces:
            if (unit, v4_prefix, v4_prefix_len) in self.interfaces[if_name]:
                print 'Same Interface already %s exists'%if_name
                return True
            else:
                for i in self.interfaces[if_name]:
                    if i[0]==unit:
                        self.interfaces[if_name][self.interfaces[if_name].index(i)]=(unit, v4_prefix, v4_prefix_len)
                        print self.interfaces
            return True
        else:
            print 'Interface %s does not exists'%if_name
            raise InvalidInterfaceException('Interface %s does not exists'%if_name)

    def InterfaceExists(self, if_name, data):
        # to show case what happen when structure name is changed
        print data, data.err_code, data.traceback
        if if_name in self.interfaces:
            print 'Interface %s exists'%if_name
        else:
            print 'Interface %s does not exists'%if_name
            raise InvalidInterfaceException('Interface %s does not exists'%if_name)

    def InterfaceGet(self, if_name):
        if if_name in self.interfaces:
            if_details = self.interfaces[if_name]
            return [IF(if_name, i[0], i[1], i[2]) for i in if_details]


handler = InterfaceServiceHandler()
processor = InterfacesService.Processor(handler)
transport = TSocket.TServerSocket(port=9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print "Starting python server version 1.1.0..."
server.serve()
print "done!"
