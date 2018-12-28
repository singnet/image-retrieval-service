import pickle
import os
import sys
from  calculate_similarity_resnet import ResnetSimilarity
import sys
import os
import pickle
from PIL import Image
from nearpy import Engine
from nearpy.hashes import RandomBinaryProjections
from nearpy.distances import CosineDistance
from nearpy.distances import EuclideanDistance
import numpy as np


class ImageSimilarity():
	def __init__(self,distanceMeasure=None):
		self.res_similar= ResnetSimilarity()
		dimension = 2048
		rbp = RandomBinaryProjections('rbp', 10)
		self.engine = Engine(dimension, lshashes=[rbp],distance=EuclideanDistance())
		if distanceMeasure == "EuclideanDistance":
			self.filehandler = open("hashed_object_equilidian.pkl", 'r')
		else:
			self.filehandler = open("hashed_object.pkl", 'r')

		self.engine = pickle.load(self.filehandler)
		print("Hash Table Loaded")

	def query(self,image):
		result = []
		image_emb = self.res_similar.getMapping(image)
		image_emb = image_emb.view(-1,2048)
		image_emb = image_emb.numpy()

		N = self.engine.neighbours(image_emb[0])
		for i in range(len(N)):
		    result.append(N[i][1]git )
		    if i == 2:
		        break

		return result



# imgs = ImageSimilarity()
# pic_one1  = Image.open("./data/classed_data/val/Dog/b8f75a7e8e6def6c.jpg")
# re = imgs.query(pic_one1)
# print(re)



