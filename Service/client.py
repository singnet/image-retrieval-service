import grpc
from concurrent import futures
import time

import os
import grpc
import image_retrival_pb2
import image_retrival_pb2_grpc

from inspect import getsourcefile
import os.path
import sys
import base64
import magic

current_path = os.path.abspath(getsourcefile(lambda: 0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)

import argparse

parser = argparse.ArgumentParser()

IMG_SHAPE = (100, 100)


class ClientTest():
    def __init__(self, port='localhost:50051', image_output='client_out'):
        self.port = port
        self.image_output = image_output

    def open_grpc_channel(self):
        channel = grpc.insecure_channel(self.port)
        stub = image_retrival_pb2_grpc.SimilarImageStub(channel)
        return stub

    def send_request(self, stub, img, similarity="Test"):
        image_file = image_retrival_pb2.ImageFileIn(image=img, similarity=similarity)

        response = stub.FindSimilar(image_file)

        return response

    def close_channel(self, channel):
        pass


if __name__ == "__main__":
    with open('data/example_dataset/4f24007b18d82e7b.jpg', 'rb') as f:
        img = f.read()
        image = base64.b64encode(img).decode('utf-8')
    client_test = ClientTest()
    stub = client_test.open_grpc_channel()
    response = client_test.send_request(stub, image, similarity="Test")
    with open('img_1', 'wb') as f:
        print(magic.from_buffer(base64.b64decode(response.imageOut1), mime=True))
        f.write(base64.b64decode(response.imageOut1))
    with open('img_2', 'wb') as f:
        print(magic.from_buffer(base64.b64decode(response.imageOut2), mime=True))
        f.write(base64.b64decode(response.imageOut2))
    with open('img_3', 'wb') as f:
        print(magic.from_buffer(base64.b64decode(response.imageOut3), mime=True))
        f.write(base64.b64decode(response.imageOut3))
    with open('img_4', 'wb') as f:
        print(magic.from_buffer(base64.b64decode(response.imageOut4), mime=True))
        f.write(base64.b64decode(response.imageOut4))
    with open('img_5', 'wb') as f:
        print(magic.from_buffer(base64.b64decode(response.imageOut5), mime=True))
        f.write(base64.b64decode(response.imageOut5))
    # Image.frombytes(data=binary_image,size=(480,320),mode='RGB').save('img_1.png')
    # binary_image = base64.b64decode(response.imageOut2)
    # Image.frombytes(data=binary_image,size=(480,320),mode='RGB').save('img_2.png')
    # binary_image = base64.b64decode(response.imageOut3)
    # Image.frombytes(data=binary_image,size=(480,320),mode='RGB').save('img_3.png')
    # binary_image = base64.b64decode(response.imageOut4)
    # Image.frombytes(data=binary_image,size=(480,320),mode='RGB').save('img_4.png')
    # binary_image = base64.b64decode(response.imageOut5)
    # Image.frombytes(data=binary_image,size=(480,320),mode='RGB').save('img_5.png')
