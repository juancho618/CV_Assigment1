
import cv2 as cv
video = cv.VideoCapture('vid.mp4')

total_frames = int(video.get(cv.CAP_PROP_FRAME_COUNT))
print(total_frames)
half_frames = total_frames // 2
current_frame = 0
while True:
    ret, frame = video.read()
    if ret:
        if current_frame < half_frames:    
            frame_gaussian = cv.bilateralFilter(frame,15,75,75)              
            cv.imshow('frame', frame_gaussian)
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