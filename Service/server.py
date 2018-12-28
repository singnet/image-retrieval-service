import grpc
from concurrent import futures
import time

import image_retrival_pb2
import image_retrival_pb2_grpc

import similarImage

class SimilarImageServicer(image_retrival_pb2_grpc.SimilarImageServicer):
	def FindSimilar(self,request,context):
		responce = image_retrival_pb2.ImageFile()
		responce.value = similarImage.find_similar(request.value)
		return responce


class Server():
	def __init__(self):
		self.port = '[::]:50051'
		self.server = None

	def start_server(self):
		self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
		image_retrival_pb2_grpc.add_SimilarImageServicer_to_server(SimilarImageServicer(),self.server)
		print('Starting server. Listening on port 50051.')
		self.server.add_insecure_port(self.port)
		self.server.start()

	def stop_server(self):
		self.server.stop(0)