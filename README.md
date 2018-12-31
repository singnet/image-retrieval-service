![singnetlogo](docs/assets/singnet-logo.jpg?raw=true 'SingularityNET')

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

## Requirement

       pip install -r requirements.txt
       
       
       
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



 
