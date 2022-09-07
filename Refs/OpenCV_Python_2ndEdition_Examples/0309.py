#0309.py
import numpy as np
import cv2

img = cv2.imread('./data/lena.jpg')
text = 'Hello'
org = (50,100)
font = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(img,text, org, font, 1, (255,0,0), 2)

cv2.imshow('img', img)
cv2.imwrite('./data/sample.jpg',img)
cv2.waitKey()
cv2.destroyAllWindows()
