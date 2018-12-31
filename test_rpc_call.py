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


class TestSuiteGrpc(unittest.TestCase):
    def setUp(self):
    	self.image = Image.open('docs/assets/boy.jpg')
    	self.server = Server()
    	self.server.start_server()
    	self.client = ClientTest()

    def test_grpc_call(self):
    	stub = self.client.open_grpc_channel()
    	image1,image2,image3,image4,image5 = self.client.send_request(stub,self.image)

    	assert(Image.isImageType(image1) == True)
    	assert(Image.isImageType(image2) == True)
    	assert(Image.isImageType(image3) == True)
    	assert(Image.isImageType(image4) == True)
    	assert(Image.isImageType(image5) == True)


    	
    def tearDown(self):
        # self.client.channel.close()
        self.server.stop_server()

if __name__ == '__main__':
    suite = unittest.TestSuite()

    suite.addTest(TestSuiteGrpc("test_grpc_call"))
    unittest.main()