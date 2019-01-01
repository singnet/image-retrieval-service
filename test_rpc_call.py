import sys
sys.path.insert(0, 'Service/')

from client import ClientTest
from server import *
from PIL import Image
import unittest
import numpy as np 
import subprocess
import torch.nn as nn
import torch
from PIL import ImageChops


class TestSuiteGrpc(unittest.TestCase):
    def setUp(self):
    	self.image = Image.open("data/example_dataset/4f24007b18d82e7b.jpg")
    	self.server = Server()
    	self.server.start_server()
    	self.client = ClientTest()

    def test_grpc_call(self):
        stub = self.client.open_grpc_channel()
        image1,image2,image3,image4,image5 = self.client.send_request(stub,self.image,similarity = "Test")
        results = ["data/example_dataset/4f24007b18d82e7b.jpg",
        "data/example_dataset/c449a728be2c4144.jpg",
        "data/example_dataset/1655ed7fefd46b13.jpg",
        "data/example_dataset/c449a728be2c4144.jpg",
        "data/example_dataset/1655ed7fefd46b13.jpg"]


        image1_exp = self.image.resize((100,100))
        image2_exp = Image.open(results[1]).resize((100,100))
        image3_exp = Image.open(results[2]).resize((100,100))
        image4_exp = Image.open(results[3]).resize((100,100))
        image5_exp = Image.open(results[4]).resize((100,100))
        

        image5.save('out.jpg')
        image5_exp.save('out2.jpg')

        assert(ImageChops.difference(image1, image1_exp).getbbox() == None)
        assert(ImageChops.difference(image2, image2_exp).getbbox() == None)        
        assert(ImageChops.difference(image3, image3_exp).getbbox() == None)
        assert(ImageChops.difference(image4, image4_exp).getbbox() == None)
        assert(ImageChops.difference(image5, image5_exp).getbbox() == None)



    	
    def tearDown(self):
        # self.client.channel.close()
        self.server.stop_server()

if __name__ == '__main__':
    suite = unittest.TestSuite()

    suite.addTest(TestSuiteGrpc("test_grpc_call"))
    unittest.main()