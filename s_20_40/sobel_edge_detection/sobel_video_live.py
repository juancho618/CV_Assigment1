
import cv2 as cv
import numpy as np

video = cv.VideoCapture(0)



def find_contours_sobel(frame):
    # Convert to graycsale
    img_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Blur the image for better edge detection
    img_blur = cv.GaussianBlur(img_gray, (3,3), 0) 

    # Sobel Edge Detection
    sobelx = cv.Sobel(src=img_blur, ddepth=cv.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
    sobely = cv.Sobel(src=img_blur, ddepth=cv.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis

    abs_sobelx = cv.convertScaleAbs(sobelx)
    abs_sobely = cv.convertScaleAbs(sobely)

    edges = cv.addWeighted(abs_sobelx, 0.5, abs_sobely, 0.5, 0)
    contours, hierarchy = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    return contours

current_frame = 0
while True:
    ret, frame = video.read()
    if ret:
        frame_contours = find_contours_sobel(frame)
        frame_w_contours = cv.drawContours(frame, frame_contours, -1, (0, 255, 0), 3)       
        cv.imshow('frame', frame_w_contours)
        if cv.waitKey(1) == ord('q'):
            break
        current_frame += 1
    else:
        current_frame = 0
        video = cv.VideoCapture(0)
cv.destroyAllWindows()
video.release()