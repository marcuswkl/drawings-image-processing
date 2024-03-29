#--------------------extract drawing 01, 02, 03--------------------

import pytesseract as tess
import cv2
import numpy as np

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def execute():

    img_ori = cv2.imread("dataset/01.png", cv2.IMREAD_GRAYSCALE)
    # img_ori = cv2.imread("dataset/02.png", cv2.IMREAD_GRAYSCALE)
    # img_ori = cv2.imread("dataset/03.png", cv2.IMREAD_GRAYSCALE)
    
    thresh = 128
    img = cv2.threshold(img_ori, thresh, 255, cv2.THRESH_BINARY)[1]
    
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

# #--------------------extract drawing 04, 05--------------------
# import pytesseract as tess
# import cv2
# import numpy as np

# tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# def execute():

#     img_ori = cv2.imread("dataset/04.png", cv2.IMREAD_GRAYSCALE)
#     # img_ori = cv2.imread("dataset/05.png", cv2.IMREAD_GRAYSCALE)
    
#     thresh = 128
#     img = cv2.threshold(img_ori, thresh, 255, cv2.THRESH_BINARY)[1]
    
#     hImg,wImg = img.shape
        
#     for rows in range(5, hImg):
#         number_of_pixel = 0
#         table_top = 0
#         for columns in range(5, wImg):
#             if img[rows, columns] == 0:
#                 number_of_pixel = number_of_pixel + 1
#         if number_of_pixel >= (0.75*hImg):
#             table_top = rows
#             break
        
#     drawing = img[5:table_top, 5:wImg]
#     drawing_resize = cv2.resize(drawing, (629, 389))
    
#     cv2.imshow("Only Drawing (Extracted)", drawing_resize)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
    
#     cv2.imwrite("drawing_extracted.png", drawing)

# #--------------------extract drawing 06, 07--------------------

# import pytesseract as tess
# import cv2
# import numpy as np

# tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# def execute():

#     img_ori = cv2.imread("dataset/06.png", cv2.IMREAD_GRAYSCALE)
#     # img_ori = cv2.imread("dataset/07.png", cv2.IMREAD_GRAYSCALE)
    
#     thresh = 128
#     img = cv2.threshold(img_ori, thresh, 255, cv2.THRESH_BINARY)[1]
    
#     hImg,wImg = img.shape
    
#     for columns in range(5,wImg):
#         number_of_pixel = 0
#         table_edge = 0
#         for rows in range(5,hImg):
#             if img[rows, columns] == 0:
#                 number_of_pixel = number_of_pixel + 1
#         if number_of_pixel >= (0.75*hImg):
#             table_edge = columns
#             break
        
#     drawing = img[4:3149,4:2370]
#     drawing_resize = cv2.resize(drawing, (680, 798))
    
#     cv2.imshow("Only Drawing (Extracted)", drawing_resize)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
    
#     cv2.imwrite("drawing_extracted.png", drawing)

# #--------------------extract drawing 20--------------------

# import cv2
# import pytesseract
# import numpy as np
# import matplotlib.pyplot as plt

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# def execute():

#     img = cv2.imread("dataset/20.png", 0)
    
#     img [1547:2050, 180:1000] = 255
#     final = img[258:, 0:2363]
    
#     cv2.imshow("Drawing 20", final)
#     cv2.waitKey()
#     cv2.destroyAllWindows()
    
#     cv2.imwrite("drawing20.png", final)