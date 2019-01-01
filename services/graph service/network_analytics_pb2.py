# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: network_analytics.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='network_analytics.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x17network_analytics.proto\"\x14\n\x04\x45\x64ge\x12\x0c\n\x04\x65\x64ge\x18\x01 \x03(\t\"=\n\x05Graph\x12\r\n\x05nodes\x18\x01 \x03(\t\x12\x14\n\x05\x65\x64ges\x18\x02 \x03(\x0b\x32\x05.Edge\x12\x0f\n\x07weights\x18\x03 \x03(\x01\"?\n\x10node_betweenness\x12\x0c\n\x04node\x18\x01 \x01(\t\x12\x1d\n\x15node_centrality_value\x18\x02 \x01(\x01\"F\n\x10\x65\x64ge_betweenness\x12\x13\n\x04\x65\x64ge\x18\x01 \x01(\x0b\x32\x05.Edge\x12\x1d\n\x15\x65\x64ge_centrality_value\x18\x02 \x01(\x01\"V\n\x13MinNodeGraphRequest\x12\x15\n\x05graph\x18\x01 \x01(\x0b\x32\x06.Graph\x12\x13\n\x0bsource_node\x18\x02 \x01(\t\x12\x13\n\x0btarget_node\x18\x03 \x01(\t\"j\n\x14MinNodeGraphResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x14\n\x0cnodes_output\x18\x03 \x03(\t\x12\x1b\n\x0c\x65\x64ges_output\x18\x04 \x03(\x0b\x32\x05.Edge\"\x92\x01\n\x19MostImportantGraphRequest\x12\x15\n\x05graph\x18\x01 \x01(\x0b\x32\x06.Graph\x12\x14\n\x0csource_nodes\x18\x02 \x03(\t\x12\x14\n\x0ctarget_nodes\x18\x03 \x03(\t\x12\x0c\n\x04Type\x18\x04 \x01(\x05\x12\x12\n\nnormalized\x18\x05 \x01(\x08\x12\x10\n\x08\x64irected\x18\x06 \x01(\x08\"\xad\x01\n\x1aMostImportantGraphResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x36\n\x1bnode_betweenness_centrality\x18\x03 \x01(\x0b\x32\x11.node_betweenness\x12\x36\n\x1b\x65\x64ge_betweenness_centrality\x18\x04 \x01(\x0b\x32\x11.edge_betweenness2\xa2\x01\n\x10NetowrkAnalytics\x12=\n\x0cMinNodeGraph\x12\x14.MinNodeGraphRequest\x1a\x15.MinNodeGraphResponse\"\x00\x12O\n\x12MostImportantGraph\x12\x1a.MostImportantGraphRequest\x1a\x1b.MostImportantGraphResponse\"\x00\x62\x06proto3')
)




_EDGE = _descriptor.Descriptor(
  name='Edge',
  full_name='Edge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='edge', full_name='Edge.edge', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=27,
  serialized_end=47,
)


_GRAPH = _descriptor.Descriptor(
  name='Graph',
  full_name='Graph',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodes', full_name='Graph.nodes', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='edges', full_name='Graph.edges', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weights', full_name='Graph.weights', index=2,
      number=3, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=49,
  serialized_end=110,
)


_NODE_BETWEENNESS = _descriptor.Descriptor(
  name='node_betweenness',
  full_name='node_betweenness',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node', full_name='node_betweenness.node', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_centrality_value', full_name='node_betweenness.node_centrality_value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=112,
  serialized_end=175,
)


_EDGE_BETWEENNESS = _descriptor.Descriptor(
  name='edge_betweenness',
  full_name='edge_betweenness',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='edge', full_name='edge_betweenness.edge', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='edge_centrality_value', full_name='edge_betweenness.edge_centrality_value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=177,
  serialized_end=247,
)


_MINNODEGRAPHREQUEST = _descriptor.Descriptor(
  name='MinNodeGraphRequest',
  full_name='MinNodeGraphRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='graph', full_name='MinNodeGraphRequest.graph', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source_node', full_name='MinNodeGraphRequest.source_node', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_node', full_name='MinNodeGraphRequest.target_node', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=249,
  serialized_end=335,
)


_MINNODEGRAPHRESPONSE = _descriptor.Descriptor(
  name='MinNodeGraphResponse',
  full_name='MinNodeGraphResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='MinNodeGraphResponse.status', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='MinNodeGraphResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nodes_output', full_name='MinNodeGraphResponse.nodes_output', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='edges_output', full_name='MinNodeGraphResponse.edges_output', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=337,
  serialized_end=443,
)


_MOSTIMPORTANTGRAPHREQUEST = _descriptor.Descriptor(
  name='MostImportantGraphRequest',
  full_name='MostImportantGraphRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='graph', full_name='MostImportantGraphRequest.graph', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source_nodes', full_name='MostImportantGraphRequest.source_nodes', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_nodes', full_name='MostImportantGraphRequest.target_nodes', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Type', full_name='MostImportantGraphRequest.Type', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='normalized', full_name='MostImportantGraphRequest.normalized', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='directed', full_name='MostImportantGraphRequest.directed', index=5,
      number=6, type=8, cpp_type=7, label=1,
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
  serialized_start=446,
  serialized_end=592,
)


_MOSTIMPORTANTGRAPHRESPONSE = _descriptor.Descriptor(
  name='MostImportantGraphResponse',
  full_name='MostImportantGraphResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='MostImportantGraphResponse.status', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='MostImportantGraphResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_betweenness_centrality', full_name='MostImportantGraphResponse.node_betweenness_centrality', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='edge_betweenness_centrality', full_name='MostImportantGraphResponse.edge_betweenness_centrality', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=595,
  serialized_end=768,
)

_GRAPH.fields_by_name['edges'].message_type = _EDGE
_EDGE_BETWEENNESS.fields_by_name['edge'].message_type = _EDGE
_MINNODEGRAPHREQUEST.fields_by_name['graph'].message_type = _GRAPH
_MINNODEGRAPHRESPONSE.fields_by_name['edges_output'].message_type = _EDGE
_MOSTIMPORTANTGRAPHREQUEST.fields_by_name['graph'].message_type = _GRAPH
_MOSTIMPORTANTGRAPHRESPONSE.fields_by_name['node_betweenness_centrality'].message_type = _NODE_BETWEENNESS
_MOSTIMPORTANTGRAPHRESPONSE.fields_by_name['edge_betweenness_centrality'].message_type = _EDGE_BETWEENNESS
DESCRIPTOR.message_types_by_name['Edge'] = _EDGE
DESCRIPTOR.message_types_by_name['Graph'] = _GRAPH
DESCRIPTOR.message_types_by_name['node_betweenness'] = _NODE_BETWEENNESS
DESCRIPTOR.message_types_by_name['edge_betweenness'] = _EDGE_BETWEENNESS
DESCRIPTOR.message_types_by_name['MinNodeGraphRequest'] = _MINNODEGRAPHREQUEST
DESCRIPTOR.message_types_by_name['MinNodeGraphResponse'] = _MINNODEGRAPHRESPONSE
DESCRIPTOR.message_types_by_name['MostImportantGraphRequest'] = _MOSTIMPORTANTGRAPHREQUEST
DESCRIPTOR.message_types_by_name['MostImportantGraphResponse'] = _MOSTIMPORTANTGRAPHRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Edge = _reflection.GeneratedProtocolMessageType('Edge', (_message.Message,), dict(
  DESCRIPTOR = _EDGE,
  __module__ = 'network_analytics_pb2'
  # @@protoc_insertion_point(class_scope:Edge)
  ))
_sym_db.RegisterMessage(Edge)

Graph = _reflection.GeneratedProtocolMessageType('Graph', (_message.Message,), dict(
  DESCRIPTOR = _GRAPH,
  __module__ = 'network_analytics_pb2'
  # @@protoc_insertion_point(class_scope:Graph)
  ))
_sym_db.RegisterMessage(Graph)

node_betweenness = _reflection.GeneratedProtocolMessageType('node_betweenness', (_message.Message,), dict(
  DESCRIPTOR = _NODE_BETWEENNESS,
  __module__ = 'network_analytics_pb2'
  # @@protoc_insertion_point(class_scope:node_betweenness)
  ))
_sym_db.RegisterMessage(node_betweenness)

edge_betweenness = _reflection.GeneratedProtocolMessageType('edge_betweenness', (_message.Message,), dict(
  DESCRIPTOR = _EDGE_BETWEENNESS,
  __module__ = 'network_analytics_pb2'
  # @@protoc_insertion_point(class_scope:edge_betweenness)
  ))
_sym_db.RegisterMessage(edge_betweenness)

MinNodeGraphRequest = _reflection.GeneratedProtocolMessageType('MinNodeGraphRequest', (_message.Message,), dict(
  DESCRIPTOR = _MINNODEGRAPHREQUEST,
  __module__ = 'network_analytics_pb2'
  # @@protoc_insertion_point(class_scope:MinNodeGraphRequest)
  ))
_sym_db.RegisterMessage(MinNodeGraphRequest)

MinNodeGraphResponse = _reflection.GeneratedProtocolMessageType('MinNodeGraphResponse', (_message.Message,), dict(
  DESCRIPTOR = _MINNODEGRAPHRESPONSE,
  __module__ = 'network_analytics_pb2'
  # @@protoc_insertion_point(class_scope:MinNodeGraphResponse)
  ))
_sym_db.RegisterMessage(MinNodeGraphResponse)

MostImportantGraphRequest = _reflection.GeneratedProtocolMessageType('MostImportantGraphRequest', (_message.Message,), dict(
  DESCRIPTOR = _MOSTIMPORTANTGRAPHREQUEST,
  __module__ = 'network_analytics_pb2'
  # @@protoc_insertion_point(class_scope:MostImportantGraphRequest)
  ))
_sym_db.RegisterMessage(MostImportantGraphRequest)

MostImportantGraphResponse = _reflection.GeneratedProtocolMessageType('MostImportantGraphResponse', (_message.Message,), dict(
  DESCRIPTOR = _MOSTIMPORTANTGRAPHRESPONSE,
  __module__ = 'network_analytics_pb2'
  # @@protoc_insertion_point(class_scope:MostImportantGraphResponse)
  ))
_sym_db.RegisterMessage(MostImportantGraphResponse)



_NETOWRKANALYTICS = _descriptor.ServiceDescriptor(
  name='NetowrkAnalytics',
  full_name='NetowrkAnalytics',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=771,
  serialized_end=933,
  methods=[
  _descriptor.MethodDescriptor(
    name='MinNodeGraph',
    full_name='NetowrkAnalytics.MinNodeGraph',
    index=0,
    containing_service=None,
    input_type=_MINNODEGRAPHREQUEST,
    output_type=_MINNODEGRAPHRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='MostImportantGraph',
    full_name='NetowrkAnalytics.MostImportantGraph',
    index=1,
    containing_service=None,
    input_type=_MOSTIMPORTANTGRAPHREQUEST,
    output_type=_MOSTIMPORTANTGRAPHRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_NETOWRKANALYTICS)

DESCRIPTOR.services_by_name['NetowrkAnalytics'] = _NETOWRKANALYTICS

# @@protoc_insertion_point(module_scope)
