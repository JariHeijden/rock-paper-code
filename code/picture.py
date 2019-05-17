import numpy as np
import cv2
counterPlayer = "test"
counterAI = "test"
text = "lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum "

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, RPS = cap.read()

    # Our operations on the frame come here
                                    #x   #y            
    cv2.putText(RPS, counterPlayer, (50, 100), cv2.FONT_HERSHEY_TRIPLEX, 1.25, (0, 0, 255))
    cv2.putText(RPS, counterAI, (525, 100), cv2.FONT_HERSHEY_TRIPLEX, 1.25, (0, 0, 255))
    cv2.putText(RPS, text, (50, 400), cv2.FONT_HERSHEY_TRIPLEX, 1.25, (0, 0, 255))
   
    # Display the resulting frame
    cv2.imshow('RPS',RPS)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()