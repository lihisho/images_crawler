# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: image_service.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'image_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13image_service.proto\"&\n\x0fGetImageRequest\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\"#\n\rGetImageReply\x12\x12\n\nimage_data\x18\x01 \x01(\x0c\x32@\n\x0cImageService\x12\x30\n\x08GetImage\x12\x10.GetImageRequest\x1a\x0e.GetImageReply\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'image_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GETIMAGEREQUEST']._serialized_start=23
  _globals['_GETIMAGEREQUEST']._serialized_end=61
  _globals['_GETIMAGEREPLY']._serialized_start=63
  _globals['_GETIMAGEREPLY']._serialized_end=98
  _globals['_IMAGESERVICE']._serialized_start=100
  _globals['_IMAGESERVICE']._serialized_end=164
# @@protoc_insertion_point(module_scope)
