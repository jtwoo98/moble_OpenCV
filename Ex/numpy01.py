import cv2
import numpy as np

img = cv2.imread('./data/guang.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('guang',img)

dst1 = 255 - img
cv2.imshow('dst1',  dst1)

cv2.waitKey()
cv2.destroyAllWindows()