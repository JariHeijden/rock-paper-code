import cv2
import numpy as np

videoCapJhei = cv2.VideoCapture(1)

lower_redJhei = np.array([0, 180, 160])
upper_redJhei = np.array([15, 255, 250])

lower_greenJhei = np.array([65, 100, 80])
upper_greenJhei = np.array([95, 255, 255])

lower_blueJhei = np.array([90, 220, 100])
upper_blueJhei = np.array([120, 255, 255])

while(True):
    _, frameJhei = videoCapJhei.read(1)                 #captures the footage

    flipImgJhei = cv2.flip(frameJhei,1)
    
    hsv = cv2.cvtColor(flipImgJhei, cv2.COLOR_BGR2HSV)

    maskRedJhei = cv2.inRange(hsv, lower_redJhei, upper_redJhei)
    maskGreenJhei = cv2.inRange(hsv, lower_greenJhei, upper_greenJhei)
    maskBlueJhei = cv2.inRange(hsv, lower_blueJhei, upper_blueJhei)

    cv2.imshow('no filter',flipImgJhei)              #displays the video feed
    cv2.imshow('red', maskRedJhei)
    cv2.imshow('green', maskGreenJhei)
    cv2.imshow('blue', maskBlueJhei)

    if cv2.waitKey(20) & 0xFF == ord(' '):                  #when space is pressed the program knows to stop
        break

# When everything done, stop filming and close windows
videoCapJhei.release()
cv2.destroyAllWindows()