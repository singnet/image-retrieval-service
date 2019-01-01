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

IMG_SHAPE = (100,100)

class ClientTest():
	def __init__(self,port='localhost:50051',image_output='client_out'):
		self.port = port
		self.image_output = image_output
	def open_grpc_channel(self):
		channel = grpc.insecure_channel(self.port)
		stub = image_retrival_pb2_grpc.SimilarImageStub(channel)
		return stub
		

	def send_request(self,stub,img,similarity="EuclideanDistance"):
		out_file_name = self.image_output+'.png'
		img = img
		img = img.resize(IMG_SHAPE)
		img_b = img.tobytes()

		image_file = image_retrival_pb2.ImageFileIn(value = img_b,image_size=int(IMG_SHAPE[0]),similarity=similarity)

		responce = stub.FindSimilar(image_file)


		image1 = Image.frombytes(data=responce.imageOut1,size=IMG_SHAPE,mode='RGB')
		image2 = Image.frombytes(data=responce.imageOut2,size=IMG_SHAPE,mode='RGB')
		image3 = Image.frombytes(data=responce.imageOut3,size=IMG_SHAPE,mode='RGB')
		image4 = Image.frombytes(data=responce.imageOut4,size=IMG_SHAPE,mode='RGB')
		image5 = Image.frombytes(data=responce.imageOut5,size=IMG_SHAPE,mode='RGB')

		return image1,image2,image3,image4,image5
	
	def close_channel(self,channel):
		pass



