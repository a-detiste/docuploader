# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: metadata.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0emetadata.proto\x12\x13yoshi.docs.metadata\x1a\x1fgoogle/protobuf/timestamp.proto\"\x99\x02\n\x08Metadata\x12/\n\x0bupdate_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x10\n\x08language\x18\x04 \x01(\t\x12\x19\n\x11\x64istribution_name\x18\x05 \x01(\t\x12\x14\n\x0cproduct_page\x18\x06 \x01(\t\x12\x19\n\x11github_repository\x18\x07 \x01(\t\x12\x15\n\rissue_tracker\x18\x08 \x01(\t\x12\x0c\n\x04stem\x18\t \x01(\t\x12\x14\n\x0cserving_path\x18\n \x01(\t\x12\r\n\x05xrefs\x18\x0b \x03(\t\x12\x15\n\rxref_services\x18\x0c \x03(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'metadata_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_METADATA']._serialized_start=73
  _globals['_METADATA']._serialized_end=354
# @@protoc_insertion_point(module_scope)
