![singnetlogo](../assets/singnet-logo.jpg?raw=true 'SingularityNET')

[![CircleCI](https://circleci.com/gh/IsraelAbebe/Image-retrieval-in-pytorch.svg?style=svg)](https://circleci.com/gh/IsraelAbebe/Image-retrieval-in-pytorch)
# Image Retrieval in Pytorch
## Service User's Guide

### Welcome
This service provides image retrieval service. that means given a huge dataset of images you can query one image as input and it will return top k similar images to that given image.

## How does it work?
There is a module that returns image embeddings given a single image by passing it through a pre-trained Resnet model. The main idea is comparing the similarities between image embeddings 
as manually comparing each image and getting closer images is not feasible due to speed and computational constraints.
So we use LSH which is an algorithm for solving the approximate or exact Near Neighbor Search in high dimensional spaces. 
The idea is we pre-compare, store and save objects and when a new image is queried we will have a certain place to look for it rather than comparing with all possible images.

we use [Google Open Images Dataset v4](https://www.figure-eight.com/dataset/open-images-annotated-with-bounding-boxes/) validation as a base dataset for now.

The user must provide a request satisfying the proto descriptions
```proto
message ImageFileIn {
	string image = 1;
	string similarity = 4;
}
```
- image: a base64 encoded with 'utf-8' image.
- preferred image comparision method either `CosineDistance` or `EuclideanDistance`

The input can be both 3 channel or 2 channel images

## Using the service on the platform
The returned results has the following form: currently we return 5 images only.
```proto
message ImageFileOut {
    string imageOut1 = 4;
    string imageOut2 = 5;
    string imageOut3 = 6;
    string imageOut4 = 7;
    string imageOut5 = 8;
}
```
      
to change this strings to images you can do like :
```python
# installable via pip install python-magic
import magic
result_image = self.client.send_request(stub, self.image, self.image_type)

# the above can come from various places i.e the strings from above.
binary_image = base64.b64decode(result_image)
# As said, we can use magic to infer the file type for the given string by infering stream.
file_format = magic.from_buffer(binary_image, mime=True).split('/')[1]

with open("images/client_out2." + file_format, 'wb') as f:
    f.write(binary_image)
```