import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

directory ='./../juan'

img = cv.imread(f'{directory}/lime.jpg')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imwrite(f'{directory}/hsv.jpg', hsv)


# Threshold the HSV image to get only blue colors
lower_red = np.array([0,100,95])
upper_red = np.array([101,200,200])

mask = cv.inRange(hsv, lower_red, upper_red)
cv.imwrite(f'{directory}/mask.jpg', mask)


# Erode and dilate the mask
kernel1 = np.ones((3,3),np.uint8)
kernel2 = np.ones((5,5),np.uint8)
mask_erode = cv.erode(mask, kernel1, iterations=1)
mask_dilate = cv.dilate(mask, kernel2, iterations=1)

cv.imwrite(f'{directory}/mask_erode.jpg', mask_erode)
cv.imwrite(f'{directory}/mask_dilate.jpg', mask_dilate)


# find contours in the mask 
contours, hierarchy = cv.findContours(mask_dilate, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# Draw contours
cv.drawContours(img, contours, -1, (0, 255, 0), 2)

cv.imwrite(f'{directory}/grabbed_object.jpg', img)