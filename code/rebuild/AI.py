#file made by Thijs with help from Jari so we can have diffirent difficulties
import time, random
strAiPickJhei = ""                                  	#string so the AI can remember it's pick
tupleRPSJhei = ("Rock", "Paper", "Scissors")			#tuple for the AI to pick from
listWinTieLossTkes = ["win", "tie", "loss"]				#This will be used by the AI and later lists to "weight" the picks
listEasyDifficultyTkes = [0.50, 0.25, 0.25]			    #the weights for the easy AI
listHardDifficultyTkes = [0.25, 0.25, 0.50]			    #the weights for the hard AI

def defEasyAIJhei(listComparingValsJhei):
    strAiPickJhei = str(random.choices(listWinTieLossTkes, listEasyDifficultyTkes))				#this will pick a random gesture with taking weights into consideration. pick = string(random(win/tie/loss, weights)
    defWinLossDifficultyJhei(strAiPickJhei, listComparingValsJhei)								#calls def to look if you won and sends the pick and comparing values list to it

def defMeduimAIJhei(listComparingValsJhei):
    strUserPickJhei = listComparingValsJhei[0]													#takes the pick from the user out of the list
    intAiPointsJhei = listComparingValsJhei[1]													#takes the points already given to the AI from the list for later adition
    intUserPointsJhei = listComparingValsJhei[2]												#takes the points already given to the user from the list for later adition
    strAiPickJhei = random.choice(tupleRPSJhei)													#this is the gesture used by the "AI"

    if strAiPickJhei == strUserPickJhei:														#checks if the input given by the player and AI is the same
        strWinlossJhei = "It's a tie!"															#if it's a tie it will send this text back so we can display it in the UI

    if strAiPickJhei == "Rock":                                                                 #checks if the AI played Rock and will then look if they won or lost
        if strUserPickJhei == "Paper":                                                          #compares to user input
            intUserPointsJhei = intUserPointsJhei + 1                                           #user won so the user gets a point
            strWinlossJhei = "Paper - Rock. You Won!"                                           #this text will be send back for the UI
        elif strUserPickJhei == "Scissors":                                                     #compares to user input
            intAiPointsJhei = intAiPointsJhei + 1                                               #AI won so AI gets a point
            strWinlossJhei = "Scissors - Rock. You lost!"                                       #text for UI

    #see comments for rock
    if strAiPickJhei == "Paper":
        if strUserPickJhei == "Scissors":
            intUserPointsJhei = intUserPointsJhei + 1
            strWinlossJhei = "Scissors - Paper. You Won!"
        elif strUserPickJhei == "Rock":
            intAiPointsJhei = intAiPointsJhei + 1
            strWinlossJhei = "Rock - Paper. You lost!"

    #see comments for rock
    if strAiPickJhei == "Scissors":
        if strUserPickJhei == "Rock":
            intUserPointsJhei = intUserPointsJhei + 1
            strWinlossJhei = "Rock - Scissors. You Won!"
        elif strUserPickJhei == "Paper":
            intAiPointsJhei = intAiPointsJhei + 1
            strWinlossJhei = "Paper - Scissors. You lost!"

    #puts everything back into the list so we can use it in the main.py file
    listComparingValsJhei[0] = strUserPickJhei
    listComparingValsJhei[1] = intAiPointsJhei
    listComparingValsJhei[2] = intUserPointsJhei
    listComparingValsJhei[3] = strWinlossJhei

#see the comments for defEasyAIJhei
def defHardAIJhei(listComparingValsJhei):
    strAiPickJhei = str(random.choices(listWinTieLossTkes, listHardDifficultyTkes))
    defWinLossDifficultyJhei(strAiPickJhei, listComparingValsJhei)

def defWinLossDifficultyJhei(strAiPickJhei, listComparingValsJhei):
    #this will retrieve all needed values from the list
    strUserPickJhei = listComparingValsJhei[0]
    intAiPointsJhei = listComparingValsJhei[1]
    intUserPointsJhei = listComparingValsJhei[2]

    if "w" in strAiPickJhei:                                    #this checks for what the given string is to determine if it wil be a win
        intUserPointsJhei = intUserPointsJhei + 1               #adds a point to the user
        #if statements to see what was played to send the right string back to the UI
        if strUserPickJhei == "Rock":
            strWinlossJhei = "Rock - Scissors. You won!"
        elif strUserPickJhei == "Paper":
            strWinlossJhei = "Paper - Rock. You won!"
        else:
            strWinlossJhei = "Scissors - Paper. You won!"

    elif "t" in strAiPickJhei:                                  #this checks for a tie
        strWinlossJhei = "It's a tie!"                          #string for the UI

    else:                                                       #see comments for the win condition
        intAiPointsJhei = intAiPointsJhei + 1
        strWinlossJhei = "You lost!"
        if strUserPickJhei == "Rock":
            strWinlossJhei = "Rock - Paper. You lost!"
        elif strUserPickJhei == "Paper":
            strWinlossJhei = "Paper - Scissors. You lost!"
        else:
            strWinlossJhei = "Scissors - Rock. You lost!"

    #puts everything back into a list to send to the main.py file
    listComparingValsJhei[0] = strUserPickJhei
    listComparingValsJhei[1] = intAiPointsJhei
    listComparingValsJhei[2] = intUserPointsJhei
    listComparingValsJhei[3] = strWinlossJhei