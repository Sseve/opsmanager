# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

# import zone_pb2 as zone__pb2
from . import zone_pb2 as zone__pb2


class ZoneStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.option = channel.unary_unary(
                '/Zone/option',
                request_serializer=zone__pb2.ZoneRequest.SerializeToString,
                response_deserializer=zone__pb2.ZoneResponse.FromString,
                )


class ZoneServicer(object):
    """Missing associated documentation comment in .proto file."""

    def option(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ZoneServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'option': grpc.unary_unary_rpc_method_handler(
                    servicer.option,
                    request_deserializer=zone__pb2.ZoneRequest.FromString,
                    response_serializer=zone__pb2.ZoneResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Zone', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Zone(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def option(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Zone/option',
            zone__pb2.ZoneRequest.SerializeToString,
            zone__pb2.ZoneResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
