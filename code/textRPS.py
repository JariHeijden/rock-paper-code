#random for the AI, sys for closing when errors happen, time to delay certain things
from liveCamera import defLiveTestJhei

#test
def defTextRpsJhei():
    import random, sys, time
    rpsTupleJhei = ("Rock", "Paper", "Scissors")        #tuple for the AI to pick from
    strAiPickJhei = ""                                  #string so the AI can remember it's pick
    intRoundAmountJhei = 0                              #round amount so you can play multiple rounds
    intUserPointsJhei = 0                               #user score to keep track of how many points are awarded
    intAiPointsJhei = 0                                 #ai score to keep track of how many points are awarded
    strUserPickJhei = ""                                #the string that will be used to keep track of the choicen gesture
    xValidGestureJhei = False                           #to check if there has been given a valid gesture
    strWinLossTextJhei = ""                             #string for camera overlay
    

    #introduction of the program
    print("Rock Paper Code", "This project was made by Jari van der Heijden, Thijs van Kessel and Amin Khachiche", "We made this project so we can play rock paper scissors with a camera", sep="\n")

    while intRoundAmountJhei <= 0:          #while the number of wins is 0 or lower it will repeat to ask
        try:
            intRoundAmountJhei = int(input("How many points for a win? (1-5)\n"))
            if intRoundAmountJhei > 5:      #if the given amount is higher then 5 it wil ask again (not because errors but because of hogging the game)
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

        strAiPickJhei = random.choice(rpsTupleJhei)        #this is the gesture used by the "AI"

        #a small delay just so everything is just a bit easier to keep track off
        time.sleep(0.3)
        #tie
        if strAiPickJhei == strUserPickJhei:
            print("You both played", strAiPickJhei, "it's a tie!")
            #code for Rock
        if strAiPickJhei == "Rock":
            if strUserPickJhei == "Paper":
                print("You covered his rock using paper!\nYou won!")
                intUserPointsJhei = intUserPointsJhei + 1
            elif strUserPickJhei == "Scissors":
                print("Your scissors got destroyed with a rock...\nYou lost")
                intAiPointsJhei = intAiPointsJhei + 1
            #code for Paper
        if strAiPickJhei == "Paper":
            if strUserPickJhei == "Scissors":
                print("You've cut his paper right in half!\nYou won!")
                intUserPointsJhei = intUserPointsJhei + 1
            elif strUserPickJhei == "Rock":
                print("Your rock got covered by a measly piece of paper...\nYou lost")
                intAiPointsJhei = intAiPointsJhei + 1
            #code for Scissors
        if strAiPickJhei == "Scissors":
            if strUserPickJhei == "Rock":
                print("You obliterated his scissors!\nYou won!")
                intUserPointsJhei = intUserPointsJhei + 1
            elif strUserPickJhei == "Paper":
                print("Your paper got cut in half...\nYou lost")
                intAiPointsJhei = intAiPointsJhei + 1
        time.sleep(1)
        print("\nYour score is: ", intUserPointsJhei, "\nThe AI score is: ", intAiPointsJhei, "\n")
        #everything below this is a soft reset so you start again in this while loop
        strAiPickJhei = ""
        strUserPickJhei = ""
        time.sleep(0.5)
        xValidGestureJhei = False
        #stops here
        

    time.sleep(0.5)
    #this part is to see who won in total
    if intUserPointsJhei > intAiPointsJhei: 
        strWinLossTextJhei = "You win this game! good job!"
        defLiveTestJhei(intUserPointsJhei, intAiPointsJhei, strWinLossTextJhei)
    else:
        strWinLossTextJhei = "ohhh you lost..that's a shame"
        defLiveTestJhei(intUserPointsJhei, intAiPointsJhei, strWinLossTextJhei)