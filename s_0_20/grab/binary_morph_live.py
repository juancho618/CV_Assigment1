
import cv2 as cv
import numpy as np
video = cv.VideoCapture(0)

def find_contours(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    _, thresh = cv.threshold(gray, 127, 255, 0)
    contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    return contours

def find_contours2(frame):
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Threshold the HSV image to get only blue colors
    lower_red = np.array([0,100,95])
    upper_red = np.array([101,200,200])

    mask = cv.inRange(hsv, lower_red, upper_red)
    blurred_mask = cv.GaussianBlur(mask, (3, 3), 0)


    # Erode and dilate the mask
    kernel1 = np.ones((3,3),np.uint8)
    kernel2 = np.ones((5,5),np.uint8)
    mask_erode = cv.erode(blurred_mask, kernel1, iterations=1)
    mask_dilate = cv.dilate(blurred_mask, kernel2, iterations=1)

    # find contours in the mask 
    contours, hierarchy = cv.findContours(mask_dilate, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    return contours
  



total_frames = int(video.get(cv.CAP_PROP_FRAME_COUNT))
print(total_frames)
half_frames = total_frames // 2
current_frame = 0
while True:
    ret, frame = video.read()
    if ret:
        frame_contours = find_contours2(frame)
        frame_w_contours = cv.drawContours(frame, frame_contours, -1, (0, 255, 0), 3)       
        cv.imshow('frame', frame_w_contours)
        if cv.waitKey(1) == ord('q'):
            break
        current_frame += 1
    else:
        current_frame = 0
        video = cv.VideoCapture('video2.mp4')
cv.destroyAllWindows()
video.release()