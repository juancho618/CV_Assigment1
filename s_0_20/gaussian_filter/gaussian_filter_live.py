
import cv2 as cv
video = cv.VideoCapture(0)


current_frame = 0
while True:
    ret, frame = video.read()
    if ret:
        frame_gaussian = cv.GaussianBlur(frame,(5,5),0)              
        cv.imshow('frame', frame_gaussian)
        if cv.waitKey(1) == ord('q'):
            break
        current_frame += 1
    else:
        current_frame = 0
        video = cv.VideoCapture(0)
cv.destroyAllWindows()
video.release()