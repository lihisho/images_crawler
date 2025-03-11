import sys
import os

# Add the symlinked proto_out directory to sys.path (so we'll be able to import the generated code throughout the project)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'proto_out_symlink')))

from src.logger import get_logger
from src.services.image_service import ImageService
from concurrent import futures
import grpc
from grpc_reflection.v1alpha import reflection
import image_service_pb2 as image_service_pb2
import image_service_pb2_grpc as image_service_pb2_grpc


def serve(logger, port=50051, wait_for_termination=True):
    logger.info(f"Starting the server on port {port}")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    image_service_pb2_grpc.add_ImageServiceServicer_to_server(ImageService(logger=logger), server)
    SERVICE_NAMES = (
        image_service_pb2.DESCRIPTOR.services_by_name['ImageService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    if wait_for_termination:
        server.wait_for_termination()

if __name__ == '__main__':
    logger = get_logger('image_service_server')
    serve(logger=logger)
