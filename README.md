# Image Similarity with Siamese Networks in Pytorch

This Project implements different image similarity measures based on the following two approaches

   - [Based on Siamese Network ](http://yann.lecun.com/exdb/publis/pdf/chopra-05.pdf)which is neural network architectures that contain two or more identical subnetworks
   
   <img src="https://qph.fs.quoracdn.net/main-qimg-b90431ff9b4c60c5d69069d7bc048ff0" width=400 height=300 float-left>

   - Using resnet18 pre-trained Network to extract features and by evaluating the similarity of two images either based on cosine similarity or pairwise similarity 
   
## Description

  -  Siamese Network 
      - to train on new dataset look at  Siamese-networks-train.ipynb
      - after training on that dataset it can return simmilarity measure between images 
               
               code at  SiameseTest.py
  - Using Pretrained resent18 model
      - after feature extraction using pretrained model it calculates image simmilarity 
               
               code at  calculate_simmilarity_resnet18.py
               
          
## Requirement

       pytorch 0.4
       python3
       
             
