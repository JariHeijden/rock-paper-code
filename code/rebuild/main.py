import cv2, time, random
import numpy as np
from AI import defHardAIJhei, defMeduimAIJhei, defEasyAIJhei

intUserPoints = 0
intAIPoints = 0
intRedCount = 0
intGreenCount = 0
intBlueCount = 0
strTextMainTop = ""
strTextMainBot = ""
xDifficulty = False
strDifficulty = ""
xRoundAmount = False
intRoundAmount = -1
xPlayerPick = False
strPlayerPick = ""
strWinLoss = ""
listComparingVals = [strPlayerPick, intAIPoints, intUserPoints, strWinLoss]
strCounterPlayer = ""
strCounterAI = ""

videoCap = cv2.VideoCapture(1)

lower_red = np.array([0, 180, 160])
upper_red = np.array([30, 255, 255])

lower_green = np.array([65, 100, 80])
upper_green = np.array([95, 255, 255])

lower_blue = np.array([90, 220, 100])
upper_blue = np.array([120, 255, 255])

while(True):

    _, frame = videoCap.read(1)                 #captures the footage
    flipImg = cv2.flip(frame,1)
        
    hsv = cv2.cvtColor(flipImg, cv2.COLOR_BGR2HSV)

    maskRed = cv2.inRange(hsv, lower_red, upper_red)
    maskGreen = cv2.inRange(hsv, lower_green, upper_green)
    maskBlue = cv2.inRange(hsv, lower_blue, upper_blue)

    cv2.putText(flipImg, strTextMainTop, (5, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255))
    cv2.putText(flipImg, strTextMainBot, (5, 450), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255))

    cv2.putText(flipImg, strCounterPlayer, (50, 110), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255))             #the text overlay
    cv2.putText(flipImg, strCounterAI, (525, 110), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255))                #the text overlay

    cv2.imshow("Rock-paper-code",flipImg)              #displays the video feed

    '''if cv2.waitKey(20) & 0xFF == ord(" "):
        intRedCount = cv2.countNonZero(maskRed)
        intGreenCount = cv2.countNonZero(maskGreen)
        intBlueCount = cv2.countNonZero(maskBlue)'''

    if xDifficulty == False:
        strTextMainBot = "Please select difficulty"
        if cv2.waitKey(20) & 0xFF == ord(" "):
            intRedCount = cv2.countNonZero(maskRed)
            intGreenCount = cv2.countNonZero(maskGreen)
            intBlueCount = cv2.countNonZero(maskBlue)
            if intGreenCount > intRedCount and intGreenCount > intBlueCount:
                strDifficulty = "Easy"
                xDifficulty = True
            elif intBlueCount > intGreenCount and intBlueCount > intRedCount:
                strDifficulty = "Normal"
                xDifficulty = True
            else:
                strDifficulty = "Hard"
                xDifficulty = True
    
    if xDifficulty == True:
        if xRoundAmount == False:
            strTextMainTop = strDifficulty
            strTextMainBot = "Best out off?"
            if cv2.waitKey(20) & 0xFF == ord(" "):
                intRedCount = cv2.countNonZero(maskRed)
                intGreenCount = cv2.countNonZero(maskGreen)
                intBlueCount = cv2.countNonZero(maskBlue)

                if intGreenCount > intRedCount and intGreenCount > intBlueCount:
                    intRoundAmount = 1
                    strTextMainBot = "Who ever wins this"
                    time.sleep(1.0)
                    xRoundAmount = True
                elif intBlueCount > intRedCount and intBlueCount > intGreenCount:
                    intRoundAmount = 2
                    strTextMainBot = "Best out of 3"
                    time.sleep(1.0)
                    xRoundAmount = True
                else:
                    intRoundAmount = 3
                    strTextMainBot = "Best out of 5"
                    time.sleep(1.0)
                    xRoundAmount = True
        
    if intRoundAmount > intUserPoints and intRoundAmount > intAIPoints:
        strTextMainTop = ""
        if cv2.waitKey(20) & 0xFF == ord(" "):
            intRedCount = cv2.countNonZero(maskRed)
            intGreenCount = cv2.countNonZero(maskGreen)
            intBlueCount = cv2.countNonZero(maskBlue)

            if intRedCount > intBlueCount and intRedCount > intGreenCount:
                strPlayerPick = "Paper"
                xPlayerPick = True
            elif intBlueCount > intRedCount and intBlueCount > intGreenCount:
                strPlayerPick = "Scissors"
                xPlayerPick = True
            else:
                strPlayerPick = "Rock"
                xPlayerPick = True

            if xPlayerPick == True:
                listComparingVals[0] = strPlayerPick
                listComparingVals[1] = intAIPoints
                listComparingVals[2] = intUserPoints

                if strDifficulty == "Easy":
                    defEasyAIJhei(listComparingVals)
                elif strDifficulty == "Normal":
                    defMeduimAIJhei(listComparingVals)
                else:
                    defHardAIJhei(listComparingVals)

                strPlayerPick = listComparingVals[0]
                intAIPoints = listComparingVals[1]
                intUserPoints = listComparingVals[2]
                strWinLoss = listComparingVals[3]
                
                strTextMainBot = strWinLoss

                strCounterPlayer = str(intUserPoints)
                strCounterAI = str(intAIPoints)
                xPlayerPick = False

    if intRoundAmount == intUserPoints:
        strTextMainBot = "You won the game!"
        strTextMainTop = strTextMainBot
        if cv2.waitKey(20) & 0xFF == ord(" "):
            break
    
    if intRoundAmount == intAIPoints:
        strTextMainBot = "You lost the game..."
        strTextMainTop = strTextMainBot
        if cv2.waitKey(20) & 0xFF == ord(" "):
            break
    

# When everything done, stop filming and close windows
cv2.destroyAllWindows()
videoCap.release()