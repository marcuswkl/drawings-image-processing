# CSC2014: Digital Imaging Processing
# Coursework / Assignment 2021
# Group Members:
# 1. Marcus Wong Ke Lun 18126672
# 2. Ko Jia Xin 17102674
# 3. Seow Yee Ying 18047449
# 4. Thum Yong Jie 19023233

import numpy as np
import cv2
from matplotlib import pyplot as pt
import pytesseract as ptsr
import openpyxl as px

ptsr.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Requirement 1
# Able to identify and extract the drawing number (e.g. SU BOL E 01 27 09 10 B) from the set of engineering drawings given to you and save them into an Excel file.

# Requirement 2
# Able to also extract other information (e.g. drawing title, author, status, etc.) from the title block and save them into an Excel file. The contents should match with the respective field titles extracted from the engineering drawing.

# Requirement 3
# Able to identify and extract the drawing (only the drawing) and save it into a separate image file with .png extension.

# Requirement 4
# Able to handle an additional engineering drawing with layout design not known to you (will not be “very different” from the engineering drawings given to you).