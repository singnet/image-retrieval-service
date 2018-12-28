from inspect import getsourcefile
import os.path
import sys

current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)


from imageSimilarity import ImageSimilarity
from PIL import Image
import numpy as np


def find_similar(input_image,Img_similarity=None):
	try:
		image = Image.frombytes(data=input_image,size=(480,320),mode='RGB')
	except:
		image = Image.frombytes(data=input_image,size=(480,320),mode='L')
		image = image.convert('RGB')

	if ImageSimilarity == None:
		imgs = ImageSimilarity()
	else:
		imgs = Img_similarity


	re = imgs.query(pic_one1)
	print(re)

	#remove
	a = np.zeros((200,200))
	number = 2

	img_out = Image.fromarray(a)

	img = img_out.convert('L').tobytes() 

	return img


# imgs = ImageSimilarity()
# pic_one1  = Image.open("./data/classed_data/val/Dog/b8f75a7e8e6def6c.jpg")
# pic_b = pic_one1.tobytes() 
# a = findSimilar(pic_b,imgs)
# print(type(a))


