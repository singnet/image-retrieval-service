import torchvision
import torchvision.datasets as dset
import torchvision.transforms as transforms
from torch.utils.data import DataLoader,Dataset
import torchvision.utils
import numpy as np
import random
from PIL import Image
import torch
from torch.autograd import Variable
import PIL.ImageOps    
import torch.nn as nn
from torch import optim
import torch.nn.functional as F
from SiameseNetworks import SiameseNetwork,SiameseNetworkDataset,ContrastiveLoss 	


class SiameseTest():
	def __init__(self,model_path):
		self.net = SiameseNetwork().cuda()
		self.net.load_state_dict(torch.load(model_path))
		self.transform=transforms.Compose([transforms.Resize(64),
                                                               transforms.RandomResizedCrop(256),
                                                               transforms.RandomHorizontalFlip(),
                                                               transforms.RandomRotation(10),
                                                               transforms.ToTensor(),
                                                               transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))])

	def getDistance(self,img_1,img_2):
		img = Variable(self.transform(img_1)).cuda()
		img = img.view(1,3,256,256)

		img2 = Variable(self.transform(img_2)).cuda()
		img2 = img2.view(1,3,256,256)

		self.net.eval()
		output1,output2 = self.net(img,img2)
		euclidean_distance = F.pairwise_distance(output1, output2)

		return torch.sum(euclidean_distance).item()





# pic_one = Image.open("./data/flower_data/train/1/image_06734.jpg")
# pic_two = Image.open("./data/flower_data/train/1/image_06734.jpg")
# pic_3 = Image.open("./data/download.jpeg")	

# res = SiameseTest("model_augmented.pt")
# value = res.getDistance(pic_one,pic_two)
# valuec = res.getDistance(pic_one,pic_3)
# print(value,valuec)


