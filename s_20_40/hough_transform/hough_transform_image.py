import cv2 as cv

import numpy as np
import matplotlib.pyplot as plt

directory ='./../../lime_canny'

img = cv.imread(f'{directory}/lime.jpg')

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

threshold_value = 100
max_value = 255
_, binary_img = cv.threshold(img_gray, threshold_value, max_value, cv.THRESH_BINARY)

# Canny Edge Detection
edges = cv.Canny(img_gray, threshold1=100, threshold2=200) # Canny Edge Detection
lines = cv.HoughLines(edges, rho=1, theta=np.pi/180, threshold=100)
for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
                
#lines = cv.HoughLinesP(edges, 1, np.pi/180, max_value, minLineLength=10, maxLineGap=250)
# print(lines_1)

# Display Sobel Edge Detection Images
cv.imshow('Image', img)
cv.waitKey(0)

 

 