import cv2 as cv
from tqdm import tqdm
# Load the image
img = cv.imread('img_lime.jpg')

# Convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# values from 0 to 255 increasing by 5 as array
thresh_values = range(0, 255, 5)

for t in tqdm(thresh_values):
    print('Threshold value: ' + str(t))
    ret, thresh = cv.threshold(gray, t, 255, cv.THRESH_BINARY)
    cv.imwrite('./thresholding/thresh_' + str(t) + '.jpg', thresh)

# Apply thresholding
# ret, thresh = cv.threshold(gray, 10, 255, cv.THRESH_BINARY)

# Apply binary morphological operations
# kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE , (5, 5)) #MORPH_RECT
# eroded = cv.erode(thresh, kernel, iterations=1)
# dilated = cv.dilate(eroded, kernel, iterations=1)

# # Find contours
# contours, hierarchy = cv.findContours(dilated, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# # Draw a rectangle around the object
# for contour in contours:
#     x, y, w, h = cv.boundingRect(contour)
#     cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# # Display the result
# cv.imshow('Image', img)
# cv.waitKey(0)
# cv.destroyAllWindows()
