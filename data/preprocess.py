from os import listdir
from os.path import isfile, join
import cv2
import csv
import os
from PIL import Image

from progressbar import ProgressBar
pbar = ProgressBar()

with open('class-descriptions-boxable.csv') as csvfile:
    data_class = list(csv.reader(csvfile))

def getclass(label):
	for i in range(len(data_class)):
		if data_class[i][0]==label:
			return data_class[i][1]


save_to = "classed_data/"

folder = "validation/"
images = [f for f in listdir(folder) if isfile(join(folder, f))]

with open('validation-annotations-bbox.csv') as csvfile:
    data = list(csv.reader(csvfile))



Xmin_idx = 0
Xmax_idx = 0
Ymin_idx = 0
Ymax_idx = 0

for i in pbar(range(len(images))):
	image_path = images[i]
	fname,ext = os.path.splitext(image_path)
	image =  Image.open(folder+image_path)
	img_width = image.size[0]
	img_height = image.size[1]

	for i in data:
		if i[0] == fname:
			Xmin_idx = int(float(i[4])*img_width)
			Xmax_idx = int(float(i[5])*img_width)
			Ymin_idx = int(float(i[6])*img_height)
			Ymax_idx = int(float(i[7])*img_height)

			class_label = getclass(i[2])
			if not os.path.exists(save_to+class_label):
				os.makedirs(save_to+class_label)
			cropped_img = image.crop((Xmin_idx,Ymin_idx,Xmax_idx,Ymax_idx))
			cropped_img.save(save_to+class_label+'/'+str(image_path))
		

		




