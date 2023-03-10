
import cv2 as cv
video = cv.VideoCapture('vid.mp4')

while True:
    ret, frame = video.read()
    if ret:      
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('gray', gray)
        if cv.waitKey(1) == ord('q'):
            break
    else:
        video = cv.VideoCapture('vid.mp4')
cv.destroyAllWindows()
video.release()