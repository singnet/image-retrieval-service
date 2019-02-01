FROM ubuntu:18.04


RUN apt-get update && apt-get install -y --no-install-recommends \
        git \
        build-essential \
        python3.6 \
        python3.6-dev \
        python3-pip \
        python-setuptools \
        cmake \
        wget \
        curl \
        libsm6 \
        libxext6 \ 
        libxrender-dev


RUN python3.6 -m pip install -U pip
RUN python3.6 -m pip install --upgrade setuptools
# Download Dataset
# Download HASH TABLES
COPY requirements.txt /tmp

WORKDIR /tmp

RUN python3.6 -m pip install -r requirements.txt
# RUN python3.6 -m pip install grpcio grpcio-tools

COPY . /Image-retrieval-in-pytorch

WORKDIR /Image-retrieval-in-pytorch

EXPOSE 8001

EXPOSE 50051

RUN cd Service && python3.6 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. image_retrival.proto

RUN ./install.sh

CMD ["python3.6", "start_service.py"]