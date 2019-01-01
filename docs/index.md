![singnetlogo](assets/singnet-logo.jpg?raw=true 'SingularityNET')

# Image Retrieval in Pytorch
## Service User's Guide

### Welcome
This service provides image retrieval service. that means given a huge dataset of images you can query one image as input and it will return top k similar images to that given image.

## How does it work?
There is a module that returns image embeddings given a single image by passing it through a pre-trained Resnet model. the main idea is comparing the similarities between image embeddings 
but manually comparing each image and getting closer images is not feasible due to speed and reputation constraints.
so we use LSH which is an algorithm for solving the approximate or exact Near Neighbor Search in high dimensional spaces. the idea is we pre compare, store and save objects and when a new image is queried we will have a certain place to look for it rather than comparing with all possible images.

we use [Google Open Images Dataset v4](https://www.figure-eight.com/dataset/open-images-annotated-with-bounding-boxes/) as a base dataset


The user must provide a request satisfying the [proto descriptions](https://github.com/IsraelAbebe/Image-retrieval-in-pytorch/blob/master/Service/image_retrival.proto) . That are:
- `PIL Image` converted to bytes using : `PIL.Image..tobytes()`
- image `size:` assuming image is square 
- prefered image comparision mathod either `CosineDistance` or `EuclideanDistance`

The input can be both # channel or 2 channel images


## Using the service on the platform
The returned result has the following form:

      message ImageFileOut {
        bytes imageOut1 = 4;
        bytes imageOut2 = 5;
        bytes imageOut3 = 6;
        bytes imageOut4 = 7;
        bytes imageOut5 = 8;
      }
      
where each image is size provided during the request

to get top 5 images images you can do like :
      
      `# where responce.imageOut1 is the first output
      image1 = Image.frombytes(data=responce.imageOut1,size=IMG_SHAPE,mode='RGB')
       `
