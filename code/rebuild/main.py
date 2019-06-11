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

videoCap = cv2.VideoCapture(1)              #makes sure the right camera is selected

#arrays to later select between different HSV values
lower_red = np.array([0, 180, 160])
upper_red = np.array([30, 255, 255])

lower_green = np.array([65, 100, 80])
upper_green = np.array([95, 255, 255])

lower_blue = np.array([90, 220, 100])
upper_blue = np.array([120, 255, 255])

while(True):

    _, frame = videoCap.read(1)                 #captures the footage
    flipImg = cv2.flip(frame,1)                 #Mirrors the video
        
    hsv = cv2.cvtColor(flipImg, cv2.COLOR_BGR2HSV)          #applys a HSV filter to the video

    maskRed = cv2.inRange(hsv, lower_red, upper_red)        #makes HSV pixels between the selected arrays true(white) and the other false(black)
    maskGreen = cv2.inRange(hsv, lower_green, upper_green)  #makes HSV pixels between the selected arrays true(white) and the other false(black)
    maskBlue = cv2.inRange(hsv, lower_blue, upper_blue)     #makes HSV pixels between the selected arrays true(white) and the other false(black)

    cv2.putText(flipImg, strTextMainTop, (5, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255))                  #the text overlay
    cv2.putText(flipImg, strTextMainBot, (5, 450), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255))                 #the text overlay

    cv2.putText(flipImg, strCounterPlayer, (50, 110), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255))             #the text overlay
    cv2.putText(flipImg, strCounterAI, (525, 110), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255))                #the text overlay

    cv2.imshow("Rock-paper-code",flipImg)              #displays the video feed

    if xDifficulty == False:                            #makes sure the first thing that happens is a difficulty select
        strTextMainBot = "Please select difficulty"
        if cv2.waitKey(20) & 0xFF == ord(" "):          #if "SpaceBar" is pressed get the following values
            intRedCount = cv2.countNonZero(maskRed)             #counts the true Red pixels
            intGreenCount = cv2.countNonZero(maskGreen)         #counts the true Green pixels
            intBlueCount = cv2.countNonZero(maskBlue)           #counts the true Blue pixels
            if intGreenCount > intRedCount and intGreenCount > intBlueCount:    #if green has the most True pixels
                strDifficulty = "Easy"
                xDifficulty = True
            elif intBlueCount > intGreenCount and intBlueCount > intRedCount:   #if blue has the most True pixels
                strDifficulty = "Normal"
                xDifficulty = True
            else:                                                               #if red has the most True pixels
                strDifficulty = "Hard"
                xDifficulty = True
    
    if xDifficulty == True:
        if xRoundAmount == False:                                               #if the difficulty is selected we have to make sure a round amount is also selected
            strTextMainTop = strDifficulty
            strTextMainBot = "Best out off?"
            if cv2.waitKey(20) & 0xFF == ord(" "):                              #if space is pressed get these values
                intRedCount = cv2.countNonZero(maskRed)             #counts the true Red pixels
                intGreenCount = cv2.countNonZero(maskGreen)         #counts the true Green pixels
                intBlueCount = cv2.countNonZero(maskBlue)           #counts the true Blue pixels

                if intGreenCount > intRedCount and intGreenCount > intBlueCount:    #if the most green
                    intRoundAmount = 1
                    strTextMainBot = "Who ever wins this"
                    time.sleep(1.0)
                    xRoundAmount = True
                elif intBlueCount > intRedCount and intBlueCount > intGreenCount:   #if the most blue
                    intRoundAmount = 2
                    strTextMainBot = "Best out of 3"
                    time.sleep(1.0)
                    xRoundAmount = True
                else:                                                               #if the most red
                    intRoundAmount = 3
                    strTextMainBot = "Best out of 5"
                    time.sleep(1.0)
                    xRoundAmount = True
        
    if intRoundAmount > intUserPoints and intRoundAmount > intAIPoints:             #if there is still more rounds then points left
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

            if xPlayerPick == True:                                             #if there is a sign selected it puts it into a list to call diffirent defs
                listComparingVals[0] = strPlayerPick
                listComparingVals[1] = intAIPoints
                listComparingVals[2] = intUserPoints
#here it will select the difficulty
                if strDifficulty == "Easy":
                    defEasyAIJhei(listComparingVals)
                elif strDifficulty == "Normal":
                    defMeduimAIJhei(listComparingVals)
                else:
                    defHardAIJhei(listComparingVals)

#here it takes the values the def "spits out" back from the list
                strPlayerPick = listComparingVals[0]
                intAIPoints = listComparingVals[1]
                intUserPoints = listComparingVals[2]
                strWinLoss = listComparingVals[3]
                
                strTextMainBot = strWinLoss

                strCounterPlayer = str(intUserPoints)
                strCounterAI = str(intAIPoints)
                xPlayerPick = False

#this is to see if the user won
    if intRoundAmount == intUserPoints:
        strTextMainBot = "You won the game!"
        strTextMainTop = strTextMainBot
        if cv2.waitKey(20) & 0xFF == ord(" "):
            break
#this is to see if the AI won
    if intRoundAmount == intAIPoints:
        strTextMainBot = "You lost the game..."
        strTextMainTop = strTextMainBot
        if cv2.waitKey(20) & 0xFF == ord(" "):
            break
    

# When everything done, stop filming and close windows
cv2.destroyAllWindows()
videoCap.release()