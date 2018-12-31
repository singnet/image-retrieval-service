import grpc
from concurrent import futures
import time

import os
import grpc
import image_retrival_pb2
import image_retrival_pb2_grpc

from PIL import Image

from inspect import getsourcefile
import os.path
import sys

current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)


import argparse

parser = argparse.ArgumentParser()

class ClientTest():
	def __init__(self,port='localhost:50051',image_output='client_out'):
		self.port = port
		self.image_output = image_output
	def open_grpc_channel(self):
		channel = grpc.insecure_channel(self.port)
		stub = image_retrival_pb2_grpc.SimilarImageStub(channel)
		return stub

	def send_request(self,stub,img):
		out_file_name = self.image_output+'.png'
		img = img
		img = img.resize((100,100))
		img_b = img.tobytes()

		image_file = image_retrival_pb2.ImageFile(value = img_b,similarity="EuclideanDistance")

		responce = stub.FindSimilar(image_file)

		image = Image.frombytes(data=responce.value,size=(100,100),mode='RGB')

		return image
	
	def close_channel(self,channel):
		pass



if __name__ == "__main__":
    img = Image.open('ex/a.jpg')
    client_test = ClientTest()
    stub = client_test.open_grpc_channel()
    image = client_test.send_request(stub,img)
    image.save('out.jpg')