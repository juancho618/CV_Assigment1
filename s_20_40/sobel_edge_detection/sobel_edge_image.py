import cv2 as cv

import numpy as np
import matplotlib.pyplot as plt

directory ='./../lime_sobel'

img = cv.imread(f'{directory}/lime.jpg')


# Convert to graycsale
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img_blur = cv.GaussianBlur(img_gray, (3,3), 0) 

# Sobel Edge Detection
sobelx = cv.Sobel(src=img_blur, ddepth=cv.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
sobely = cv.Sobel(src=img_blur, ddepth=cv.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis

abs_sobelx = cv.convertScaleAbs(sobelx)
abs_sobely = cv.convertScaleAbs(sobely)

edges = cv.addWeighted(abs_sobelx, 0.5, abs_sobely, 0.5, 0)
cv.imshow('edges', edges)
cv.waitKey(0)
contours, hierarchy = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# Draw contours
cv.drawContours(img, contours, -1, (0, 0, 255), 2)
# Display Sobel Edge Detection Images
cv.imshow('Image', img)
cv.waitKey(0)

 
# Canny Edge Detection
# edges = cv.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
# # Display Canny Edge Detection Image
# cv.imshow('Canny Edge Detection', edges)
# cv.waitKey(0)
 