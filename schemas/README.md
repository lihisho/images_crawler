# Crawler Schemas

## Installation

#### Make sure you are under the correct directory
> cd schemas

#### Create a virtual env
> python3.11 -m venv .venv

#### Activate the virtual env (in case your IDE doesn't by default)
> source .venv/bin/activate

#### Install dependencies
> pip install -r requirements.txt

## Usage

#### To generate/update proto schemas run
> python -m grpc_tools.protoc -I./protos --python_out=./out --grpc_python_out=./out ./protos/*.proto
