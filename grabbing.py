import cv2 as cv

# Load the video
cap = cv.VideoCapture('video2.mp4')

# Create a window to display the video
cv.namedWindow('Video')

# Loop through the frames
while True:
    # Read a frame from the video
    ret, frame = cap.read()
    
    # Convert the frame to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    # Detect the object using a technique such as template matching or contour detection
    # You can replace this with your own code to detect the object
    # Here, we're just drawing a rectangle around the center of the frame
    height, width = gray.shape
    x = int(width/2 - 50)
    y = int(height/2 - 50)
    cv.rectangle(frame, (x, y), (x+100, y+100), (0, 255, 0), 2)
    
    # Display the video in the window
    cv.imshow('Video', frame)
    
    # Wait for a key press before moving to the next frame
    if cv.waitKey(1) == ord('q'):
        break

# Release the video and close the window
cap.release()
cv.destroyAllWindows()