from calculate_similarity_resnet import ResnetSimilarity

from PIL import Image
from progressbar import ProgressBar

from nearpy import Engine
from nearpy.hashes import RandomBinaryProjections
from nearpy.distances import CosineDistance
from nearpy.distances import EuclideanDistance

import sys

import pickle
import os
from nearpy.storage import MemoryStorage
import numpy as np


class GenerateHashTable():
    def __init__(self, measure="EuclideanDistance",data_path = 'data/classed_data/'):
        self.res = ResnetSimilarity()
        self.pbar = ProgressBar()
        # Dimension of our vector space
        self.dimension = 2048
        self.data_path = data_path

        # Create a random binary hash with 10 bits
        self.rbp = RandomBinaryProjections('rbp', 10)

        self.measure = measure
        self.msote = MemoryStorage()
        if measure=="EuclideanDistance":
            self.engine = Engine(self.dimension, lshashes=[self.rbp], storage=self.msote, distance=EuclideanDistance())
        else:
            self.engine = Engine(self.dimension, lshashes=[self.rbp], storage=self.msote, distance=CosineDistance())

    def generate_table(self):
        if self.measure == "CosineDistance":
            save_path = "hashed_objects/hashed_object_Cosine.pkl"
        elif self.measure == "EuclideanDistance":
            save_path = "hashed_objects/hashed_object_equilidian.pkl"
        else:
            save_path = "hashed_objects/"+str(self.measure)+".pkl"

        count = 0
        for subdir, dirs, files in os.walk(self.data_path):
            for file in files:
                if '.jpg' in file :
                    img_path = os.path.join(subdir, file)
                    img = Image.open(img_path).convert('RGB')

                    if img.size[0] >= 100:
                        img_emb = self.res.getMapping(img)
                        img_emb = img_emb.view(-1, 2048)
                        img_emb = img_emb.numpy()

                        self.engine.store_vector(img_emb[0], img_path)
                        if count % 1000 == 0:
                            print("Saving  Image Embedding ", count)
                        count += 1

        print("Saving File To",save_path)
        filehandler = open("hashed_object_equilidian.pkl", 'wb')
        pickle.dump(engine, filehandler)




if __name__ == "__main__":
    image_sim_eq = GenerateHashTable(measure="EuclideanDistance",data_path = 'data/classed_data/')
    image_sim_eq.generate_table()
    image_sim_cos = GenerateHashTable(measure="CosineDistance",data_path = 'data/classed_data/')
    image_sim_cos.generate_table()