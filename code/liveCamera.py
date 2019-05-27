import numpy as np
import cv2

def defLiveOverlayAkha(intUserPointsJhei, intAiPointsJhei, strWinLossTextJhei):

    strCounterPlayerAkha = str(intUserPointsJhei)               #this will convert the points of the user to a string for later diplay
    strCounterAIAkha = str(intAiPointsJhei)                     #converts ai points for later display            

    videoCapAkha = cv2.VideoCapture(0)                          #so it knows to use either an internal or an external camera

    while(True):
        ret, frameRPSAkha = videoCapAkha.read(1)                 #captures the footage

        flipImgAkha = cv2.flip(frameRPSAkha,1)
        
        cv2.putText(flipImgAkha, strCounterPlayerAkha, (50, 110), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255))             #the text overlay
        cv2.putText(flipImgAkha, strCounterAIAkha, (525, 110), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255))                #the text overlay
        cv2.putText(flipImgAkha, strWinLossTextJhei, (10, 400), cv2.FONT_HERSHEY_DUPLEX, 1.10, (0, 0, 255))            #the text overlay

        cv2.imshow('Rock-Paper-Code',flipImgAkha)              #displays the video feed with the text overlay

        if cv2.waitKey(20) & 0xFF == ord(' '):                  #when space is pressed the program knows to stop
            break

    # When everything done, stop filming and close windows
    videoCapAkha.release()
    cv2.destroyAllWindows()