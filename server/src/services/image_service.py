import os
import tempfile
import grpc
import image_service_pb2 as image_service_pb2
import image_service_pb2_grpc as image_service_pb2_grpc
from icrawler.builtin import GoogleImageCrawler


class ImageService(image_service_pb2_grpc.ImageService):
    def __init__(self, logger):
        super().__init__()
        self.logger = logger

    def GetImage(self, request, context):
        self.logger.info(f"Received request: {request}")

        if not request.description:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Description cannot be empty")
            return image_service_pb2.GetImageReply()

        with tempfile.TemporaryDirectory() as temp_dir:

            # Initialize the GoogleImageCrawler
            google_crawler = GoogleImageCrawler(storage={'root_dir': temp_dir})
            google_crawler.logger = self.logger

            # Crawl and download a single image
            google_crawler.crawl(keyword=request.description, max_num=1)
            image_bytes = None

            # Get the path of the downloaded image
            for dirpath, _, files in os.walk(temp_dir):
                if not files:
                    self.logger.info(f'Didn\'t find any image for the requested description: {request.description}')
                    context.set_code(grpc.StatusCode.NOT_FOUND)
                    context.set_details("Image not found")
                    return image_service_pb2.GetImageReply()

                image_path = os.path.join(dirpath, files[0])

                # Read the bytes of the downloaded file
                with open(image_path, 'rb') as img_file:
                    image_bytes = img_file.read()

            # Send the image in chunks
            chunk_size = 1024 * 1024  # 1MB
            for i in range(0, len(image_bytes), chunk_size):
                chunk = image_bytes[i:i + chunk_size]
                response = image_service_pb2.GetImageReply(image_data=chunk)
                yield response
