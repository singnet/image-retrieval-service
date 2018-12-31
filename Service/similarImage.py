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


def find_similar(input_image,Img_similarity="EuclideanDistance"):
	try:
		image = Image.frombytes(data=input_image,size=(100,100),mode='RGB')
	except:
		image = Image.frombytes(data=input_image,size=(100,100),mode='L')
		image = image.convert('RGB')

	# imgs = ImageSimilarity()
	print(Img_similarity)

	if ImageSimilarity == "CosineDistance":
		imgs = ImageSimilarity(distanceMeasure="CosineDistance")
	else:
		imgs = ImageSimilarity(distanceMeasure="EuclideanDistance")


	re = imgs.query(image)
	print(re)

	image_1 = Image.open(re[0]).resize((100,100))
	image_2 = Image.open(re[1]).resize((100,100))
	image_3 = Image.open(re[2]).resize((100,100))

	image_1_b = image_1.tobytes()
	image_2_b = image_2.tobytes()
	image_3_b = image_3.tobytes()

	return image_2_b


# imgs = ImageSimilarity()
# pic_one1  = Image.open("./data/classed_data/val/Dog/b8f75a7e8e6def6c.jpg")
# pic_b = pic_one1.tobytes() 
# a = findSimilar(pic_b,imgs)
# print(type(a))


