# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mix.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mix.proto',
  package='mouthwash',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\tmix.proto\x12\tmouthwash\x1a\x1bgoogle/protobuf/empty.proto\"5\n\x0bShotElement\x12\x12\n\ninstrument\x18\x01 \x01(\t\x12\x12\n\nparamNames\x18\x02 \x01(\x0c\"6\n\x0bIngredients\x12\x12\n\ninstrument\x18\x01 \x01(\t\x12\x13\n\x0bparamValues\x18\x02 \x01(\x0c\"R\n\x11ShotReviewSummary\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04good\x18\x02 \x01(\x05\x12\x10\n\x08waittime\x18\x03 \x01(\x02\x12\x0f\n\x07timeout\x18\x04 \x01(\x08\x32\x8d\x01\n\x05Mixer\x12>\n\nMixANewOne\x12\x16.mouthwash.ShotElement\x1a\x16.mouthwash.Ingredients\"\x00\x12\x44\n\nShotReview\x12\x1c.mouthwash.ShotReviewSummary\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_SHOTELEMENT = _descriptor.Descriptor(
  name='ShotElement',
  full_name='mouthwash.ShotElement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instrument', full_name='mouthwash.ShotElement.instrument', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paramNames', full_name='mouthwash.ShotElement.paramNames', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=106,
)


_INGREDIENTS = _descriptor.Descriptor(
  name='Ingredients',
  full_name='mouthwash.Ingredients',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instrument', full_name='mouthwash.Ingredients.instrument', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paramValues', full_name='mouthwash.Ingredients.paramValues', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=162,
)


_SHOTREVIEWSUMMARY = _descriptor.Descriptor(
  name='ShotReviewSummary',
  full_name='mouthwash.ShotReviewSummary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mouthwash.ShotReviewSummary.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='good', full_name='mouthwash.ShotReviewSummary.good', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='waittime', full_name='mouthwash.ShotReviewSummary.waittime', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='mouthwash.ShotReviewSummary.timeout', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=164,
  serialized_end=246,
)

DESCRIPTOR.message_types_by_name['ShotElement'] = _SHOTELEMENT
DESCRIPTOR.message_types_by_name['Ingredients'] = _INGREDIENTS
DESCRIPTOR.message_types_by_name['ShotReviewSummary'] = _SHOTREVIEWSUMMARY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ShotElement = _reflection.GeneratedProtocolMessageType('ShotElement', (_message.Message,), {
  'DESCRIPTOR' : _SHOTELEMENT,
  '__module__' : 'mix_pb2'
  # @@protoc_insertion_point(class_scope:mouthwash.ShotElement)
  })
_sym_db.RegisterMessage(ShotElement)

Ingredients = _reflection.GeneratedProtocolMessageType('Ingredients', (_message.Message,), {
  'DESCRIPTOR' : _INGREDIENTS,
  '__module__' : 'mix_pb2'
  # @@protoc_insertion_point(class_scope:mouthwash.Ingredients)
  })
_sym_db.RegisterMessage(Ingredients)

ShotReviewSummary = _reflection.GeneratedProtocolMessageType('ShotReviewSummary', (_message.Message,), {
  'DESCRIPTOR' : _SHOTREVIEWSUMMARY,
  '__module__' : 'mix_pb2'
  # @@protoc_insertion_point(class_scope:mouthwash.ShotReviewSummary)
  })
_sym_db.RegisterMessage(ShotReviewSummary)



_MIXER = _descriptor.ServiceDescriptor(
  name='Mixer',
  full_name='mouthwash.Mixer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=249,
  serialized_end=390,
  methods=[
  _descriptor.MethodDescriptor(
    name='MixANewOne',
    full_name='mouthwash.Mixer.MixANewOne',
    index=0,
    containing_service=None,
    input_type=_SHOTELEMENT,
    output_type=_INGREDIENTS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ShotReview',
    full_name='mouthwash.Mixer.ShotReview',
    index=1,
    containing_service=None,
    input_type=_SHOTREVIEWSUMMARY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MIXER)

DESCRIPTOR.services_by_name['Mixer'] = _MIXER

# @@protoc_insertion_point(module_scope)