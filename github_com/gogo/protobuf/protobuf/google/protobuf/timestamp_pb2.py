# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: github_com/gogo/protobuf/protobuf/google/protobuf/timestamp.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='github_com/gogo/protobuf/protobuf/google/protobuf/timestamp.proto',
  package='google.protobuf',
  syntax='proto3',
  serialized_pb=_b('\nAgithub_com/gogo/protobuf/protobuf/google/protobuf/timestamp.proto\x12\x0fgoogle.protobuf\"+\n\tTimestamp\x12\x0f\n\x07seconds\x18\x01 \x01(\x03\x12\r\n\x05nanos\x18\x02 \x01(\x05\x42X\n\x13\x63om.google.protobufB\x0eTimestampProtoP\x01Z\x05types\xf8\x01\x01\xa2\x02\x03GPB\xaa\x02\x1eGoogle.Protobuf.WellKnownTypesb\x06proto3')
)




_TIMESTAMP = _descriptor.Descriptor(
  name='Timestamp',
  full_name='google.protobuf.Timestamp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seconds', full_name='google.protobuf.Timestamp.seconds', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nanos', full_name='google.protobuf.Timestamp.nanos', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=86,
  serialized_end=129,
)

DESCRIPTOR.message_types_by_name['Timestamp'] = _TIMESTAMP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Timestamp = _reflection.GeneratedProtocolMessageType('Timestamp', (_message.Message,), dict(
  DESCRIPTOR = _TIMESTAMP,
  __module__ = 'github_com.gogo.protobuf.protobuf.google.protobuf.timestamp_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.Timestamp)
  ))
_sym_db.RegisterMessage(Timestamp)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\023com.google.protobufB\016TimestampProtoP\001Z\005types\370\001\001\242\002\003GPB\252\002\036Google.Protobuf.WellKnownTypes'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
