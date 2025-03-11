# Images Crawler
This project is a Kivy-based application that allows users to fetch images from a gRPC server by providing a description. The application communicates with the server using gRPC and displays the fetched images.

## Prerequisites
- Python 3.11

## Installation and usage
Follow the README.md files instructions in each project:
- schemas
- server
- client

Run the schemas first, then the server and then the client in different terminals - each using its own virtual environment (venv).

## Project structure
- schemas/: Contains the Protocol Buffers definitions and generated code.
- server/: Contains the gRPC server implementation.
- client/: Contains the client application code.
