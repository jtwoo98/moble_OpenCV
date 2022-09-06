# 0202.py
import cv2

imageFile = './data/lena.jpg'
img = cv2.imread(imageFile) 
cv2.imwrite('./data/Lena.bmp', img)
cv2.imwrite('./data/Lena.png', img)
cv2.imwrite('./data/Lena2.png',img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
cv2.imwrite('./data/Lena2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 5])



img  = cv2.imread('./data/Lena.bmp')    # cv2.IMREAD_COLOR
img2 = cv2.imread('./data/Lena2.jpg',0)

cv2.imshow('Lena bmp',img)
cv2.imshow('Lena png',img2)

cv2.waitKey()
cv2.destroyAllWindows()