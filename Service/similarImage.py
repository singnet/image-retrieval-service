from inspect import getsourcefile
import os.path
import sys

current_path = os.path.abspath(getsourcefile(lambda: 0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)

from imageSimilarity import ImageSimilarity
from PIL import Image
import numpy as np
import base64
import tempfile
import magic


def find_similar(input_image, image_size=100, img_similarity="EuclideanDistance"):
    # IMG_SHAPE = (image_size, image_size)
    binary_image = base64.b64decode(input_image)
    file_format = magic.from_buffer(base64.b64decode(input_image), mime=True).split('/')[1]

    f = tempfile.NamedTemporaryFile(suffix='*.' + str(file_format))
    f.write(binary_image)
    image = Image.open(f.name)

    if img_similarity == "CosineDistance":
        imgs = ImageSimilarity(distanceMeasure="CosineDistance")
    elif img_similarity == "Test":
        imgs = ImageSimilarity(distanceMeasure="Test")
    else:
        imgs = ImageSimilarity(distanceMeasure="EuclideanDistance")

    re = imgs.query(image)
    imgs.tearDown()

    # Why resize the response file.
    image = []
    for i in re:
        with open(i, 'rb') as f:
            img = f.read()
            img = base64.b64encode(img).decode('utf-8')
        image.append(img)


    return image[0], image[1], image[2], image[3], image[4]

# imgs = ImageSimilarity()
# pic_one1  = Image.open("./data/classed_data/val/Dog/b8f75a7e8e6def6c.jpg")
# pic_b = pic_one1.tobytes() 
# a = findSimilar(pic_b,imgs)
# print(type(a))
