# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: weather.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import reflection as _reflection
from google.protobuf import message as _message
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rweather.proto\x12\x07weather\"!\n\x0eWeatherRequest\x12\x0f\n\x07\x61pi_key\x18\x01 \x01(\t\"\'\n\x0fWeatherResponse\x12\x14\n\x0cjson_message\x18\x01 \x01(\t2N\n\x08Reporter\x12\x42\n\rWeatherReport\x12\x17.weather.WeatherRequest\x1a\x18.weather.WeatherResponseb\x06proto3')

_WEATHERREQUEST = DESCRIPTOR.message_types_by_name['WeatherRequest']
_WEATHERRESPONSE = DESCRIPTOR.message_types_by_name['WeatherResponse']

WeatherRequest = _reflection.GeneratedProtocolMessageType('WeatherRequest',(_message.Message,),{
  'DESCRIPTOR' : _WEATHERREQUEST,
  '__module__' : 'weather_pb2'
  # @@protoc_insertion_point(class_scope:weather.WeatherRequest)
})
_sym_db.RegisterMessage(WeatherRequest)

WeatherResponse = _reflection.GeneratedProtocolMessageType('WeatherResponse',(_message.Message,),{
  'DESCRIPTOR' : _WEATHERRESPONSE,
  '__module__' : 'weather_pb2'
  # @@protoc_insertion_point(class_scope:weather.WeatherResponse)
})
_sym_db.RegisterMessage(WeatherResponse)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'weather_pb2', globals())
_REPORTER = DESCRIPTOR.services_by_name['Reporter']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _WEATHERREQUEST._serialized_start=26
  _WEATHERREQUEST._serialized_end=59
  _WEATHERRESPONSE._serialized_start=61
  _WEATHERRESPONSE._serialized_end=100
  _REPORTER._serialized_start=102
  _REPORTER._serialized_end=180
# @@protoc_insertion_point(module_scope)

