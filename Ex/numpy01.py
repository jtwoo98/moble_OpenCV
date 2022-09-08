import cv2
import numpy as np

img = cv2.imread('./data/lena.jpg',cv2.IMREAD_GRAYSCALE)

cv2.imwrite('./data/Lena13.png', img)