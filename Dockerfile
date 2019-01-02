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
# COPY requirements.txt /tmp
# WORKDIR /tmp
RUN python3.6 -m pip install matplotlib  numpy==1.15.1  Pillow==5.3.0  torch==1.0.0  torchvision==0.2.1  argparse==1.4.0  jupyter==1.0.0  jupyter-client==5.2.3  jupyter-console==5.2.0  jupyter-core==4.4.0  jupyterlab==0.34.9  jupyterlab-launcher==0.13.1  NearPy==1.0.0  pickle-mixin==1.0.2  grpcio==1.17.0  grpcio-tools==1.17.0  ipykernel==4.9.0  ipython==6.5.0  ipython-genutils==0.2.0  ipywidgets==7.4.1  progressbar==2.5  
# RUN python3.6 -m pip install grpcio grpcio-tools

COPY . /Image-retrieval-in-pytorch

WORKDIR /Image-retrieval-in-pytorch

EXPOSE 8001

EXPOSE 50051

RUN cd Service && python3.6 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. image_retrival.proto

CMD ["python3.6", "start_service.py"]