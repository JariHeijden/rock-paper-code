from textRPS import *
import numpy as np
import cv2

def defLiveTestJhei(intUserPointsJhei, intAiPointsJhei, strWinLossTextJhei):

    counterPlayer = str(intUserPointsJhei)
    counterAI = str(intAiPointsJhei)
    text = strWinLossTextJhei

    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, RPS = cap.read()

        # Our operations on the frame come here
                                        #x   #y            
        cv2.putText(RPS, counterPlayer, (50, 110), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255))
        cv2.putText(RPS, counterAI, (525, 110), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255))
        cv2.putText(RPS, text, (10, 400), cv2.FONT_HERSHEY_DUPLEX, 1.10, (0, 0, 255))
    
        # Display the resulting frame
        cv2.imshow('RPS',RPS)

        if cv2.waitKey(20) & 0xFF == ord(' '):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()