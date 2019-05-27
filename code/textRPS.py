#time to delay certain things
import time
from AI import defHardAIJhei, defMeduimAIJhei, defEasyAIJhei
from liveCamera import defLiveOverlayAkha

def defTextRpsJhei():
    intRoundAmountJhei = 0                              #round amount so you can play multiple rounds
    intUserPointsJhei = 0                               #user score to keep track of how many points are awarded
    intAiPointsJhei = 0                                 #ai score to keep track of how many points are awarded
    strUserPickJhei = ""                                #the string that will be used to keep track of the choicen gesture
    xValidGestureJhei = False                           #to check if there has been given a valid gesture
    strWinLossTextJhei = ""                             #string for camera overlay
    str_intDifficultyJhei = ""                          #string to decide difficulty
    xDifficultySelectJhei = False                       #to keep asking difficulty when not defined

    #introduction of the program
    print("Rock Paper Code", "This project was made by Jari van der Heijden, Thijs van Kessel and Amin Khachiche", "We made this project so we can play rock paper scissors with a camera", sep="\n")
    
    str_intDifficultyJhei = input("Do you want to play easy, medium or hard mode?\n")
    
    while xDifficultySelectJhei == False:
        if "ea" in str_intDifficultyJhei.lower():
            str_intDifficultyJhei = 1
            xDifficultySelectJhei = True
        elif "me" in str_intDifficultyJhei.lower():
            str_intDifficultyJhei = 2
            xDifficultySelectJhei = True
        elif "ha" in str_intDifficultyJhei.lower():
            str_intDifficultyJhei = 3
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
            strUserPickJhei = input("Pick: Rock, paper or scissors?\n")                     #this input will be used for picking a gesture
            #this is a spell check if the input is close to valid and then turns it into something we can surrely use
            if "ro" in strUserPickJhei.lower():
                strUserPickJhei = "Rock"
                xValidGestureJhei = True
            elif "pa" in strUserPickJhei.lower():
                strUserPickJhei = "Paper"
                xValidGestureJhei = True
            elif "sc" in strUserPickJhei.lower():
                strUserPickJhei = "Scissors"
                xValidGestureJhei = True

        
        listComparingValsJhei = [strUserPickJhei, intAiPointsJhei, intUserPointsJhei]
        #a small delay just so everything is just a bit easier to keep track off
        time.sleep(0.3)

        if str_intDifficultyJhei == 1:
            defEasyAIJhei(listComparingValsJhei)
        elif str_intDifficultyJhei == 2:
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