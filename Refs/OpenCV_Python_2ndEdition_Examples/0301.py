#0301.py
import cv2
import numpy as np

imageFile = './data/lena.jpg'
img  = cv2.imread(imageFile) 
#img = np.ones((512,512,3), np.uint8) * 255
#img = np.full((512,512,3), (255, 255, 255), dtype= np.uint8)
#img = np.zeros((512,512, 3), np.uint8) # Black 배경
pt1 = 100, 100
pt2 = 400, 400
cv2.rectangle(img, pt1, pt2, (0, 0, 0), 30)

cv2.line(img, (240, 100), (100, 200), (0, 0, 0), 30)
cv2.line(img, (240, 100), (400, 200), (0,0,0), 30)

cv2.imshow('img', img)
cv2.imwrite('./data/Lena12.png', img)

cv2.waitKey()
cv2.destroyAllWindows()
