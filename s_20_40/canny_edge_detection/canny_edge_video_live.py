import cv2 as cv
import numpy as np

video = cv.VideoCapture(0)



def find_contours_canny(frame):
    # Convert to graycsale
    img_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Blur the image for better edge detection
    img_blur = cv.GaussianBlur(img_gray, (3,3), 0) 

    # Canny Edge Detection
    edges = cv.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
    contours, hierarchy = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    return contours

current_frame = 0
while True:
    ret, frame = video.read()
    if ret:
        frame_contours = find_contours_canny(frame)
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
 