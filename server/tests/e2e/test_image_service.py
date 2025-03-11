from server import serve
from src.logger import get_logger
import unittest
import grpc
import image_service_pb2 as image_service_pb2
import image_service_pb2_grpc as image_service_pb2_grpc


class TestImageService(unittest.TestCase):
    def setUp(self):
        logger = get_logger("test_image_service_e2e")

        # Create a gRPC server
        self.port = 50052
        serve(logger, self.port, wait_for_termination=False)

        # Create a gRPC channel and stub
        self.channel = grpc.insecure_channel(f'localhost:{self.port}')
        self.stub = image_service_pb2_grpc.ImageServiceStub(self.channel)

    def tearDown(self):
        self.channel.close()

    def test_get_image_success(self):
        # Create a request
        request = image_service_pb2.GetImageRequest(description='puppies')

        # Call the service
        responses = self.stub.GetImage(request)

        # Collect all chunks
        image_data = b''
        for response in responses:
            image_data += response.image_data

        # Check if image data is received
        self.assertTrue(len(image_data) > 0)

    def test_get_image_no_results(self):
            # Create a request
            request = image_service_pb2.GetImageRequest(description='')

            # Call the service
            responses = self.stub.GetImage(request)

            error = None
            try:
                # Collect all chunks
                image_data = b''
                for response in responses:
                    image_data += response.image_data
            except grpc.RpcError as exc:
                error = exc

            self.assertIsNotNone(error)
            self.assertEqual(grpc.StatusCode.INVALID_ARGUMENT, error.code())
            self.assertEqual('Description cannot be empty', error.details())


if __name__ == '__main__':
    unittest.main()
