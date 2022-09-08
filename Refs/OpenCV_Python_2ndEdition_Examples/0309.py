#0309.py
import numpy as np
import cv2

#sudo raspistill -o .jpg

img = cv2.imread('./data/lena.jpg')
text = 'Hello'
org = (50,100)
font = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(img,text, org, font, 1, (255,0,0), 2)

cv2.imwrite('./data/sample.jpg',img)

