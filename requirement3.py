def execute():
    print("Requirement 3 Code")

#extract drawing 01, 02, 03

import pytesseract as tess
import cv2
import numpy as np

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img_ori = cv2.imread("01.png", cv2.IMREAD_GRAYSCALE)
# img_ori = cv2.imread("02.png", cv2.IMREAD_GRAYSCALE)
# img_ori = cv2.imread("03.png", cv2.IMREAD_GRAYSCALE)

thresh = 128
img = cv2.threshold(img_ori, thresh, 255, cv2.THRESH_BINARY)[1]

img_contours = img.copy()

hImg,wImg = img.shape

for columns in range(5,wImg):
    number_of_pixel = 0
    table_edge = 0
    for rows in range(5,hImg):
        if img[rows, columns] == 0:
            number_of_pixel = number_of_pixel + 1
    if number_of_pixel >= (0.75*hImg):
        table_edge = columns
        break
    
drawing = img[4:3149,4:table_edge]
drawing_resize = cv2.resize(drawing, (328, 629))

cv2.imshow("Only Drawing (Extracted)", drawing_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("drawing_extracted.png", drawing)