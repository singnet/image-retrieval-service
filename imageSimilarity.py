import pickle
import os
import sys
from calculate_similarity_resnet import ResnetSimilarity
import sys
import os
import _pickle as pickle
from PIL import Image
from nearpy import Engine
from nearpy.hashes import RandomBinaryProjections
from nearpy.distances import CosineDistance
from nearpy.distances import EuclideanDistance
import numpy as np


class ImageSimilarity():
    def __init__(self, distanceMeasure="EuclideanDistance"):
        self.res_similar = ResnetSimilarity()
        dimension = 2048
        rbp = RandomBinaryProjections('rbp', 10)
        self.engine = Engine(dimension, lshashes=[rbp])
        if distanceMeasure == "EuclideanDistance":
            self.filehandler = open("hashed_objects/hashed_object_equilidian.pkl", 'rb')
        elif distanceMeasure == "Test":
            self.filehandler = open("hashed_objects/hashed_object_example.pkl", 'rb')
        else:
            self.filehandler = open("hashed_objects/hashed_object_Cosine.pkl", 'rb')
        self.engine = pickle.load(self.filehandler)
        self.filehandler.close()
        print("Hash Table Loaded")

    def query(self, image):
        result = []
        image_emb = self.res_similar.getMapping(image)
        image_emb = image_emb.view(-1, 2048)
        image_emb = image_emb.numpy()

        N = self.engine.neighbours(image_emb[0])
        for i in range(len(N)):
            result.append(N[i][1])
            if i == 5:
                break

        return result

    def tearDown(self):
        self.filehandler.close()
