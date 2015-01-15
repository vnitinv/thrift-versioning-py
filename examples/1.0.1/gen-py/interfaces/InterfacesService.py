#
# Autogenerated by Thrift Compiler (0.9.1)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface:
  def V4InterfaceAdd(self, if_name, unit, prefix, prefix_len):
    """
    Parameters:
     - if_name
     - unit
     - prefix
     - prefix_len
    """
    pass

  def V4InterfaceDelete(self, if_name, unit, prefix, prefix_len):
    """
    Parameters:
     - if_name
     - unit
     - prefix
     - prefix_len
    """
    pass

  def V4InterfaceEdit(self, if_name, unit, prefix, prefix_len):
    """
    Parameters:
     - if_name
     - unit
     - prefix
     - prefix_len
    """
    pass

  def InterfaceExists(self, if_name, ret_status):
    """
    Parameters:
     - if_name
     - ret_status
    """
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def V4InterfaceAdd(self, if_name, unit, prefix, prefix_len):
    """
    Parameters:
     - if_name
     - unit
     - prefix
     - prefix_len
    """
    self.send_V4InterfaceAdd(if_name, unit, prefix, prefix_len)
    return self.recv_V4InterfaceAdd()

  def send_V4InterfaceAdd(self, if_name, unit, prefix, prefix_len):
    self._oprot.writeMessageBegin('V4InterfaceAdd', TMessageType.CALL, self._seqid)
    args = V4InterfaceAdd_args()
    args.if_name = if_name
    args.unit = unit
    args.prefix = prefix
    args.prefix_len = prefix_len
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_V4InterfaceAdd(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = V4InterfaceAdd_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "V4InterfaceAdd failed: unknown result");

  def V4InterfaceDelete(self, if_name, unit, prefix, prefix_len):
    """
    Parameters:
     - if_name
     - unit
     - prefix
     - prefix_len
    """
    self.send_V4InterfaceDelete(if_name, unit, prefix, prefix_len)
    return self.recv_V4InterfaceDelete()

  def send_V4InterfaceDelete(self, if_name, unit, prefix, prefix_len):
    self._oprot.writeMessageBegin('V4InterfaceDelete', TMessageType.CALL, self._seqid)
    args = V4InterfaceDelete_args()
    args.if_name = if_name
    args.unit = unit
    args.prefix = prefix
    args.prefix_len = prefix_len
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_V4InterfaceDelete(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = V4InterfaceDelete_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "V4InterfaceDelete failed: unknown result");

  def V4InterfaceEdit(self, if_name, unit, prefix, prefix_len):
    """
    Parameters:
     - if_name
     - unit
     - prefix
     - prefix_len
    """
    self.send_V4InterfaceEdit(if_name, unit, prefix, prefix_len)
    return self.recv_V4InterfaceEdit()

  def send_V4InterfaceEdit(self, if_name, unit, prefix, prefix_len):
    self._oprot.writeMessageBegin('V4InterfaceEdit', TMessageType.CALL, self._seqid)
    args = V4InterfaceEdit_args()
    args.if_name = if_name
    args.unit = unit
    args.prefix = prefix
    args.prefix_len = prefix_len
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_V4InterfaceEdit(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = V4InterfaceEdit_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ae is not None:
      raise result.ae
    raise TApplicationException(TApplicationException.MISSING_RESULT, "V4InterfaceEdit failed: unknown result");

  def InterfaceExists(self, if_name, ret_status):
    """
    Parameters:
     - if_name
     - ret_status
    """
    self.send_InterfaceExists(if_name, ret_status)
    self.recv_InterfaceExists()

  def send_InterfaceExists(self, if_name, ret_status):
    self._oprot.writeMessageBegin('InterfaceExists', TMessageType.CALL, self._seqid)
    args = InterfaceExists_args()
    args.if_name = if_name
    args.ret_status = ret_status
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_InterfaceExists(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = InterfaceExists_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.ae is not None:
      raise result.ae
    return


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["V4InterfaceAdd"] = Processor.process_V4InterfaceAdd
    self._processMap["V4InterfaceDelete"] = Processor.process_V4InterfaceDelete
    self._processMap["V4InterfaceEdit"] = Processor.process_V4InterfaceEdit
    self._processMap["InterfaceExists"] = Processor.process_InterfaceExists

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_V4InterfaceAdd(self, seqid, iprot, oprot):
    args = V4InterfaceAdd_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = V4InterfaceAdd_result()
    result.success = self._handler.V4InterfaceAdd(args.if_name, args.unit, args.prefix, args.prefix_len)
    oprot.writeMessageBegin("V4InterfaceAdd", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_V4InterfaceDelete(self, seqid, iprot, oprot):
    args = V4InterfaceDelete_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = V4InterfaceDelete_result()
    result.success = self._handler.V4InterfaceDelete(args.if_name, args.unit, args.prefix, args.prefix_len)
    oprot.writeMessageBegin("V4InterfaceDelete", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_V4InterfaceEdit(self, seqid, iprot, oprot):
    args = V4InterfaceEdit_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = V4InterfaceEdit_result()
    try:
      result.success = self._handler.V4InterfaceEdit(args.if_name, args.unit, args.prefix, args.prefix_len)
    except InvalidInterfaceException, ae:
      result.ae = ae
    oprot.writeMessageBegin("V4InterfaceEdit", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_InterfaceExists(self, seqid, iprot, oprot):
    args = InterfaceExists_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = InterfaceExists_result()
    try:
      self._handler.InterfaceExists(args.if_name, args.ret_status)
    except InvalidInterfaceException, ae:
      result.ae = ae
    oprot.writeMessageBegin("InterfaceExists", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class V4InterfaceAdd_args:
  """
  Attributes:
   - if_name
   - unit
   - prefix
   - prefix_len
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'if_name', None, None, ), # 1
    (2, TType.I32, 'unit', None, None, ), # 2
    (3, TType.STRING, 'prefix', None, None, ), # 3
    (4, TType.I32, 'prefix_len', None, None, ), # 4
  )

  def __init__(self, if_name=None, unit=None, prefix=None, prefix_len=None,):
    self.if_name = if_name
    self.unit = unit
    self.prefix = prefix
    self.prefix_len = prefix_len

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.if_name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.unit = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.prefix = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.prefix_len = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('V4InterfaceAdd_args')
    if self.if_name is not None:
      oprot.writeFieldBegin('if_name', TType.STRING, 1)
      oprot.writeString(self.if_name)
      oprot.writeFieldEnd()
    if self.unit is not None:
      oprot.writeFieldBegin('unit', TType.I32, 2)
      oprot.writeI32(self.unit)
      oprot.writeFieldEnd()
    if self.prefix is not None:
      oprot.writeFieldBegin('prefix', TType.STRING, 3)
      oprot.writeString(self.prefix)
      oprot.writeFieldEnd()
    if self.prefix_len is not None:
      oprot.writeFieldBegin('prefix_len', TType.I32, 4)
      oprot.writeI32(self.prefix_len)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class V4InterfaceAdd_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (RetStatus, RetStatus.thrift_spec), None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = RetStatus()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('V4InterfaceAdd_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class V4InterfaceDelete_args:
  """
  Attributes:
   - if_name
   - unit
   - prefix
   - prefix_len
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'if_name', None, None, ), # 1
    (2, TType.I32, 'unit', None, None, ), # 2
    (3, TType.STRING, 'prefix', None, None, ), # 3
    (4, TType.I32, 'prefix_len', None, None, ), # 4
  )

  def __init__(self, if_name=None, unit=None, prefix=None, prefix_len=None,):
    self.if_name = if_name
    self.unit = unit
    self.prefix = prefix
    self.prefix_len = prefix_len

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.if_name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.unit = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.prefix = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.prefix_len = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('V4InterfaceDelete_args')
    if self.if_name is not None:
      oprot.writeFieldBegin('if_name', TType.STRING, 1)
      oprot.writeString(self.if_name)
      oprot.writeFieldEnd()
    if self.unit is not None:
      oprot.writeFieldBegin('unit', TType.I32, 2)
      oprot.writeI32(self.unit)
      oprot.writeFieldEnd()
    if self.prefix is not None:
      oprot.writeFieldBegin('prefix', TType.STRING, 3)
      oprot.writeString(self.prefix)
      oprot.writeFieldEnd()
    if self.prefix_len is not None:
      oprot.writeFieldBegin('prefix_len', TType.I32, 4)
      oprot.writeI32(self.prefix_len)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class V4InterfaceDelete_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (RetStatus, RetStatus.thrift_spec), None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = RetStatus()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('V4InterfaceDelete_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class V4InterfaceEdit_args:
  """
  Attributes:
   - if_name
   - unit
   - prefix
   - prefix_len
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'if_name', None, None, ), # 1
    (2, TType.I32, 'unit', None, None, ), # 2
    (3, TType.STRING, 'prefix', None, None, ), # 3
    (4, TType.I32, 'prefix_len', None, None, ), # 4
  )

  def __init__(self, if_name=None, unit=None, prefix=None, prefix_len=None,):
    self.if_name = if_name
    self.unit = unit
    self.prefix = prefix
    self.prefix_len = prefix_len

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.if_name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.unit = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.prefix = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.prefix_len = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('V4InterfaceEdit_args')
    if self.if_name is not None:
      oprot.writeFieldBegin('if_name', TType.STRING, 1)
      oprot.writeString(self.if_name)
      oprot.writeFieldEnd()
    if self.unit is not None:
      oprot.writeFieldBegin('unit', TType.I32, 2)
      oprot.writeI32(self.unit)
      oprot.writeFieldEnd()
    if self.prefix is not None:
      oprot.writeFieldBegin('prefix', TType.STRING, 3)
      oprot.writeString(self.prefix)
      oprot.writeFieldEnd()
    if self.prefix_len is not None:
      oprot.writeFieldBegin('prefix_len', TType.I32, 4)
      oprot.writeI32(self.prefix_len)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class V4InterfaceEdit_result:
  """
  Attributes:
   - success
   - ae
  """

  thrift_spec = (
    (0, TType.BOOL, 'success', None, None, ), # 0
    (1, TType.STRUCT, 'ae', (InvalidInterfaceException, InvalidInterfaceException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, ae=None,):
    self.success = success
    self.ae = ae

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.BOOL:
          self.success = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.ae = InvalidInterfaceException()
          self.ae.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('V4InterfaceEdit_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.BOOL, 0)
      oprot.writeBool(self.success)
      oprot.writeFieldEnd()
    if self.ae is not None:
      oprot.writeFieldBegin('ae', TType.STRUCT, 1)
      self.ae.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class InterfaceExists_args:
  """
  Attributes:
   - if_name
   - ret_status
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'if_name', None, None, ), # 1
    (2, TType.STRUCT, 'ret_status', (RetStatus, RetStatus.thrift_spec), None, ), # 2
  )

  def __init__(self, if_name=None, ret_status=None,):
    self.if_name = if_name
    self.ret_status = ret_status

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.if_name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.ret_status = RetStatus()
          self.ret_status.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('InterfaceExists_args')
    if self.if_name is not None:
      oprot.writeFieldBegin('if_name', TType.STRING, 1)
      oprot.writeString(self.if_name)
      oprot.writeFieldEnd()
    if self.ret_status is not None:
      oprot.writeFieldBegin('ret_status', TType.STRUCT, 2)
      self.ret_status.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class InterfaceExists_result:
  """
  Attributes:
   - ae
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'ae', (InvalidInterfaceException, InvalidInterfaceException.thrift_spec), None, ), # 1
  )

  def __init__(self, ae=None,):
    self.ae = ae

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.ae = InvalidInterfaceException()
          self.ae.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('InterfaceExists_result')
    if self.ae is not None:
      oprot.writeFieldBegin('ae', TType.STRUCT, 1)
      self.ae.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
