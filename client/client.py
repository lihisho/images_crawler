import sys
import os

# Add the symlinked proto_out directory to sys.path (so we'll be able to import the generated code throughout the project)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'proto_out_symlink')))

import tempfile
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
import grpc
import image_service_pb2
import image_service_pb2_grpc

stub = None

class ImageCrawlerApp(App):
    def __init__(self):
        super().__init__()
        self.stub = stub

    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        
        self.header_layout = BoxLayout(orientation='vertical', size_hint=(1, 0.1))
        input_layout = BoxLayout(orientation='horizontal', size_hint=(1, 1))
        self.error_label = Label(text="", size_hint=(1, 1))
        
        # Create a text input widget
        self.text_input = TextInput(hint_text='Enter image description', size_hint=(0.8, 1))
        input_layout.add_widget(self.text_input)

        # Create a button widget
        update_button = Button(text='Update Image', size_hint=(0.2, 1))
        update_button.bind(on_press=self.get_image)
        input_layout.add_widget(update_button)
        
        self.header_layout.add_widget(input_layout)
        # Add the header layout to the main layout
        self.layout.add_widget(self.header_layout)

        self.image = Image()
        self.layout.add_widget(self.image)

        return self.layout

    def show_error(self, message):
        self.error_label.text = message
        self.header_layout.add_widget(self.error_label)

    def hide_error(self):
        self.header_layout.remove_widget(self.error_label)

    def get_image(self, instance):
        self.hide_error()

        if not self.text_input.text:
            self.show_error("Description cannot be empty")
            return

        try:
            request = image_service_pb2.GetImageRequest(description=self.text_input.text)
            response_stream = self.stub.GetImage(request)

            # Save the image data to a temporary file
            with tempfile.NamedTemporaryFile(delete=True) as temp_file:
                for response in response_stream:
                    temp_file.write(response.image_data)
                temp_file_path = temp_file.name

                self.image.source = temp_file_path
                self.image.reload()
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                self.show_error("Image not found")
        except Exception as e:
            self.show_error(f"An unknown error occurred while fetching the image")
            print(f"An unknown error occurred while fetching the image: {e}")


if __name__ == '__main__':
    channel = grpc.insecure_channel('localhost:50051')
    stub = image_service_pb2_grpc.ImageServiceStub(channel)
    ImageCrawlerApp().run()
