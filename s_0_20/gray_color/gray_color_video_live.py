import cv2 as cv
video = cv.VideoCapture(0)
# Frames in Gray
# count frames

current_frame = 0
is_gray = False
while True:
    ret, frame = video.read()
    if ret:
        if current_frame % 100 == 0:
            is_gray = not is_gray
        if is_gray == True:      
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            cv.imshow('frame', gray)
        else:
            cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q'):
            break
        current_frame += 1
    else:
        current_frame = 0
        video = cv.VideoCapture('vid.mp4')
cv.destroyAllWindows()
video.release()