
import cv2 as cv
videos_path = './../../videos'
video = cv.VideoCapture(f'{videos_path}/vid.mp4')

total_frames = int(video.get(cv.CAP_PROP_FRAME_COUNT))
print(total_frames)
half_frames = total_frames // 2
current_frame = 0
while True:
    ret, frame = video.read()
    if ret:
        if current_frame < half_frames:      
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            cv.imshow('frame', gray)
        else:
            cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q'):
            break
        current_frame += 1
    else:
        video = cv.VideoCapture(f'{videos_path}/vid.mp4')
cv.destroyAllWindows()
video.release()