from PIL import Image
import pytesseract
import cv2 as cv
 
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract'

cimg = cv.imread('./data/drive.png')
img = cv.cvtColor(cimg, cv.COLOR_BGR2GRAY)
_, img = cv.threshold(img, 100, 255, cv.THRESH_BINARY)
cv.imwrite('./data/good.jpg',img)

str = pytesseract.image_to_string(Image.open('./data/good.jpg'), lang='kor')

 
print(str)