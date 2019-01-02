![singnetlogo](docs/assets/singnet-logo.jpg?raw=true 'SingularityNET')

[![CircleCI](https://circleci.com/gh/IsraelAbebe/Image-retrieval-in-pytorch.svg?style=svg)](https://circleci.com/gh/IsraelAbebe/Image-retrieval-in-pytorch)
# Image Retrieval in Pytorch

This Project implements image retrieval from large image dataset using different image similarity measures based on the following two approaches.

   - [Based on Siamese Network ](http://yann.lecun.com/exdb/publis/pdf/chopra-05.pdf)which is neural network architectures that contain two or more identical subnetworks
      - can be used for predefined image dataset and must be trained on that image dataset to work for our purpose 
   
   <img src="https://qph.fs.quoracdn.net/main-qimg-b90431ff9b4c60c5d69069d7bc048ff0" width=400 height=300 float-left>

   - Using Resnet pre-trained Network to extract features and store them based on LSH simmilarity to get faster responce for large dataset 

             


## Description

  -  Siamese Network 
      - to train on new dataset look at  Siamese-networks-train.ipynb
      - after training on that dataset it can return simmilarity measure between images 
               
               example code at  SiameseTest.py
  - Using Pretrained resent18 model
      - after feature extraction using pretrained model it calculates image simmilarity 
               
               example code at  storeLSH.ipynb


               
## Install prerequisites        

### Using pip

      #To install requirements for the project 
      $ pip install -r requirements.txt

      $ pip install grpcio
      $ pip install grpcio-tools

 ## Setup  
 
      run the following command to generate gRPC classes for Python

      # only in Service folder run
      $ python3.6 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. image_retrival.proto


## Usage
To run it on your own image, use the following command. Please make sure to see their paper / the code for more details.

       # on project directory this will start the server 
	   $ python  start_service.py
     
     

## Using docker with GPU

If you have a [nvidia-docker2](https://github.com/NVIDIA/nvidia-docker) installed, we have Dockerfile.gpu which you can use to build your image.

     docker build --file Dockerfile.gpu . -t singnet:image-retrieval

## Using docker with CPU

You can also build an image which has only the CPU dependecies to evaluate the models provided.

	docker build --file Dockerfile . -t singnet:image-retrieval-cpu
   
   
 ## How to Use the docker image
	
      # this will open port 50051 and run the service 
      docker run -it --rm -p 50051:50051 singnet:image-retrieval-cpu

 ## How to preprocess datasets
 - After downoading [Google Open Images Dataset v4](https://www.figure-eight.com/dataset/open-images-annotated-with-bounding-boxes/) use data/preprocess.py to put each data in their classes . i also used data/testtrainsplit.py to separate the data to folders for checking image retrieval (but this is not mandatory)
 
 ## How to generate the hash table 
- As given in storeLSH.ipynb you can initialize LSH engine and add image embedding after hashing and comparing them either by cosine similarity or Euclidean distance . then you will save the table using pickle

## Testing output
- first read the pickle file and then you can query the image you have on that hash table . it will return the index that is similar , in our case the image path


# TODO
preparing a better cleaner and good resolution data-set can improve the output results

## Authors
Israel Abebe - Author and Maintainer - [SingularityNet.io](https://singularitynet.io/)



 
