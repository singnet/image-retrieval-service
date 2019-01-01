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


def find_similar(input_image,image_size=100 ,Img_similarity="EuclideanDistance"):
	print
	IMG_SHAPE = (image_size,image_size)
	try:
		image = Image.frombytes(data=input_image,size=IMG_SHAPE,mode='RGB')
	except:
		image = Image.frombytes(data=input_image,size=IMG_SHAPE,mode='L')
		image = image.convert('RGB')

	

	if Img_similarity == "CosineDistance":
		imgs = ImageSimilarity(distanceMeasure="CosineDistance")
	if Img_similarity == "Test":
		imgs = ImageSimilarity(distanceMeasure="Test")
	else:
		imgs = ImageSimilarity(distanceMeasure="EuclideanDistance")


	re = imgs.query(image)
	imgs.tearDown()

	image_1 = Image.open(re[0]).resize(IMG_SHAPE)
	image_2 = Image.open(re[1]).resize(IMG_SHAPE)
	image_3 = Image.open(re[2]).resize(IMG_SHAPE)
	image_4= Image.open(re[3]).resize(IMG_SHAPE)
	image_5 = Image.open(re[4]).resize(IMG_SHAPE)


	image_1_b = image_1.tobytes()
	image_2_b = image_2.tobytes()
	image_3_b = image_3.tobytes()
	image_4_b = image_2.tobytes()
	image_5_b = image_3.tobytes()


	return image_1_b,image_2_b,image_3_b,image_4_b,image_5_b


# imgs = ImageSimilarity()
# pic_one1  = Image.open("./data/classed_data/val/Dog/b8f75a7e8e6def6c.jpg")
# pic_b = pic_one1.tobytes() 
# a = findSimilar(pic_b,imgs)
# print(type(a))


