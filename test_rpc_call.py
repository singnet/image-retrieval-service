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
import base64
import magic
from PIL import ImageChops


class TestSuiteGrpc(unittest.TestCase):
    def setUp(self):
        self.results = ["data/example_dataset/4f24007b18d82e7b.jpg",
                        "data/example_dataset/c449a728be2c4144.jpg",
                        "data/example_dataset/1655ed7fefd46b13.jpg",
                        "data/example_dataset/c449a728be2c4144.jpg",
                        "data/example_dataset/1655ed7fefd46b13.jpg"]

        self.image = []
        for i in self.results:
            with open(i, 'rb') as f:
                img = f.read()
                self.image.append(base64.b64encode(img).decode('utf-8'))
        self.server = Server()
        self.server.start_server()
        self.client = ClientTest()

    def test_grpc_call(self):
        stub = self.client.open_grpc_channel()
        response = self.client.send_request(stub, self.image[0], similarity="Test")

        with open('img_1', 'wb') as f:
            print(magic.from_buffer(base64.b64decode(response.imageOut1), mime=True).split('/'))
            f.write(base64.b64decode(response.imageOut1))
        with open('img_2', 'wb') as f:
            print(magic.from_buffer(base64.b64decode(response.imageOut2), mime=True).split('/'))
            f.write(base64.b64decode(response.imageOut2))
        with open('img_3', 'wb') as f:
            print(magic.from_buffer(base64.b64decode(response.imageOut3), mime=True).split('/'))
            f.write(base64.b64decode(response.imageOut3))
        with open('img_4', 'wb') as f:
            print(magic.from_buffer(base64.b64decode(response.imageOut4), mime=True).split('/'))
            f.write(base64.b64decode(response.imageOut4))
        with open('img_5', 'wb') as f:
            print(magic.from_buffer(base64.b64decode(response.imageOut5), mime=True).split('/'))
            f.write(base64.b64decode(response.imageOut5))

        with open('img_1_', 'wb') as f:
            print(magic.from_buffer(base64.b64decode(self.image[0]), mime=True).split('/'))
            f.write(base64.b64decode(self.image[0]))
        with open('img_2_', 'wb') as f:
            print(magic.from_buffer(base64.b64decode(self.image[1]), mime=True).split('/'))
            f.write(base64.b64decode(self.image[1]))
        with open('img_3_', 'wb') as f:
            print(magic.from_buffer(base64.b64decode(self.image[2]), mime=True).split('/'))
            f.write(base64.b64decode(self.image[2]))
        with open('img_4_', 'wb') as f:
            print(magic.from_buffer(base64.b64decode(self.image[3]), mime=True).split('/'))
            f.write(base64.b64decode(self.image[3]))
        with open('img_5_', 'wb') as f:
            print(magic.from_buffer(base64.b64decode(self.image[4]), mime=True).split('/'))
            f.write(base64.b64decode(self.image[4]))

        # TODO how come the above are very different when passed through it.
        # The size between the two are different.
        self.assertEquals(base64.b64decode(response.imageOut1), base64.b64decode(self.image[0]))
        self.assertEquals(base64.b64decode(response.imageOut2), base64.b64decode(self.image[1]))
        self.assertEqual(response.imageOut3, self.image[2])
        self.assertEqual(response.imageOut4, self.image[3])
        self.assertEqual(response.imageOut5, self.image[4])

    def tearDown(self):
        # self.client.channel.close()
        self.server.stop_server()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestSuiteGrpc("test_grpc_call"))
    unittest.main()
