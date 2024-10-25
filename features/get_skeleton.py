import cv2
import numpy as np
from PIL import Image

from .get_longest_distance import get_longest_distance


PIXEL2CM = 0.06


def pixel_to_cm(val):
    return PIXEL2CM * val


def get_skeleton(img):
    images = np.array(Image.open(img))
    kernel = np.ones((25, 25), np.uint8)
    images = cv2.erode(images, kernel, iterations=2)

    thinned = cv2.ximgproc.thinning(cv2.cvtColor(images, cv2.COLOR_RGB2GRAY))
    kernel = np.ones((3, 3), np.uint8)
    thinned = cv2.dilate(thinned, kernel, iterations=2)
    cv2.imwrite('static/segment/fish_segment.png', thinned)

    length_object = get_longest_distance('static/segment/fish_segment.png')
    length = pixel_to_cm(int(round(length_object.value, 0)))

    return length
