import cv2 as cv

import numpy as np
import matplotlib.pyplot as plt

directory ='./../lime_canny'

img = cv.imread(f'{directory}/lime.jpg')


# Convert to graycsale
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img_blur = cv.GaussianBlur(img_gray, (3,3), 0) 

# Canny Edge Detection
edges = cv.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
# # Display Canny Edge Detection Image
cv.imshow('Canny Edge Detection', edges)
cv.waitKey(0)
contours, hierarchy = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# Draw contours
cv.drawContours(img, contours, -1, (0, 0, 255), 2)
# Display Sobel Edge Detection Images
cv.imshow('Image', img)
cv.waitKey(0)

 

 