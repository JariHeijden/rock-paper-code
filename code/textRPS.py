#time to delay certain things
import time
from AI import defHardAIJhei, defMeduimAIJhei, defEasyAIJhei
from liveCamera import defLiveOverlayAkha
from cameraColor import defCameraColorJhei

def defTextRpsJhei():
    intRoundAmountJhei = 0                              #round amount so you can play multiple rounds
    intUserPointsJhei = 0                               #user score to keep track of how many points are awarded
    intAiPointsJhei = 0                                 #ai score to keep track of how many points are awarded
    xValidGestureJhei = False                           #to check if there has been given a valid gesture
    strWinLossTextJhei = ""                             #string for camera overlay
    intDifficultyJhei = ""                          #string to decide difficulty
    strUserPickJhei = ""                                #the string that will be used to keep track of the choicen gesture
    xDifficultySelectJhei = False                       #to keep asking difficulty when not defined
    intRedJhei = 0
    intBlueJhei = 0
    intGreenJhei = 0
    strGesCheckJhei = ""

    #introduction of the program
    print("Rock Paper Code", "This project was made by Jari van der Heijden, Thijs van Kessel and Amin Khachiche", "We made this project so we can play rock paper scissors with a camera", sep="\n")
    
    while xDifficultySelectJhei == False:

        print("Please select a difficulty")

        listCameraJhei = [intRedJhei, intBlueJhei, intGreenJhei]
        defCameraColorJhei(listCameraJhei)
        intRedJhei = listCameraJhei[0]
        intGreenJhei = listCameraJhei[1]
        intBlueJhei = listCameraJhei[2]
        if intGreenJhei > intRedJhei and intGreenJhei > intBlueJhei:
            intDifficultyJhei = 1
        elif intBlueJhei > intRedJhei and intGreenJhei < intBlueJhei:
            intDifficultyJhei = 2
        else:
            intDifficultyJhei = 3

        if intDifficultyJhei == 1:
            print("You selecteded easy difficulty")
        elif intDifficultyJhei == 2:
            print("You selected meduim difficulty")
        else:
            print("You selected hard difficulty")
        xDifficultySelectJhei = True
        

    while intRoundAmountJhei <= 0:          #while the number of wins is 0 or lower it will repeat to ask
        try:
            intRoundAmountJhei = int(input("How many points do you need to win the whole game? (1-5)\n"))
            if intRoundAmountJhei > 5:      #if the given amount is higher then 5 it wil ask again (not because errors but because of long games being boring after a while)
                print("Please enter a number between 1-5")
                intRoundAmountJhei = 0
        except:
            print("Please enter a number between 1-5")

    while intRoundAmountJhei > intUserPointsJhei and intRoundAmountJhei > intAiPointsJhei:  #this will make sure the rock paper scissors keeps repeating for the amount of rounds selected
        while xValidGestureJhei == False:                                                   #checks if there is valid input for comparing else repeat
            
            listCameraJhei = [intRedJhei, intBlueJhei, intGreenJhei]
            defCameraColorJhei(listCameraJhei)
            intRedJhei = listCameraJhei[0]
            intGreenJhei = listCameraJhei[1]
            intBlueJhei = listCameraJhei[2]
            
            if intRedJhei > intBlueJhei and intRedJhei > intGreenJhei:
                strUserPickJhei = "Paper"
            elif intBlueJhei > intRedJhei and intBlueJhei > intGreenJhei:
                strUserPickJhei = "Scissors"
            else:
                strUserPickJhei = "Rock"

            print("You picked:", strUserPickJhei)
            strGesCheckJhei = input("Is this correct?\n")
            if "y" in strGesCheckJhei.lower():
                xValidGestureJhei = True
        
        listComparingValsJhei = [strUserPickJhei, intAiPointsJhei, intUserPointsJhei]
        #a small delay just so everything is just a bit easier to keep track off
        time.sleep(0.3)

        if intDifficultyJhei == 1:
            defEasyAIJhei(listComparingValsJhei)
        elif intDifficultyJhei == 2:
            defMeduimAIJhei(listComparingValsJhei)
        else:
            defHardAIJhei(listComparingValsJhei)
        xValidGestureJhei = False

        strUserPickJhei = listComparingValsJhei[0]
        intAiPointsJhei = listComparingValsJhei[1]
        intUserPointsJhei = listComparingValsJhei[2]

    time.sleep(0.5)
    #this part is to see who won in total
    if intUserPointsJhei > intAiPointsJhei: 
        strWinLossTextJhei = "You won this game! good job!"
        defLiveOverlayAkha(intUserPointsJhei, intAiPointsJhei, strWinLossTextJhei)     #this will send the string and 2 ints to a diffirent file
    else:
        strWinLossTextJhei = "ohhh you lost..that's a shame"
        defLiveOverlayAkha(intUserPointsJhei, intAiPointsJhei, strWinLossTextJhei)     #this will send the string and 2 ints to a diffirent file