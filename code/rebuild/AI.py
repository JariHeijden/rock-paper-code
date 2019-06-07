import time, random
strAiPickJhei = ""                                  #string so the AI can remember it's pick
tupleRPSJhei = ("Rock", "Paper", "Scissors")        #tuple for the AI to pick from
listWinTieLostTkes = ["win", "tie", "loss"]
listEasyDifficultyTkes = [0.50, 0.25, 0.25]
listHardDifficultyTkes = [0.25, 0.25, 0.50]

def defEasyAIJhei(listComparingValsJhei):
    strAiPickJhei = str(random.choices(listWinTieLostTkes, listEasyDifficultyTkes))
    defWinLossDifficultyJhei(strAiPickJhei, listComparingValsJhei)

def defMeduimAIJhei(listComparingValsJhei):
    strUserPickJhei = listComparingValsJhei[0]
    intAiPointsJhei = listComparingValsJhei[1]
    intUserPointsJhei = listComparingValsJhei[2]
    strAiPickJhei = random.choice(tupleRPSJhei)        #this is the gesture used by the "AI"

    if strAiPickJhei == strUserPickJhei:
        strWinlossJhei = "It's a tie!"

    if strAiPickJhei == "Rock":
        if strUserPickJhei == "Paper":
            intUserPointsJhei = intUserPointsJhei + 1
            strWinlossJhei = "Rock. You Won!"
        elif strUserPickJhei == "Scissors":
            intAiPointsJhei = intAiPointsJhei + 1
            strWinlossJhei = "Rock. You lost!"

        #code for Paper
    if strAiPickJhei == "Paper":
        if strUserPickJhei == "Scissors":
            intUserPointsJhei = intUserPointsJhei + 1
            strWinlossJhei = "Paper. You Won!"
        elif strUserPickJhei == "Rock":
            intAiPointsJhei = intAiPointsJhei + 1
            strWinlossJhei = "Paper. You lost!"
            
        #code for Scissors
    if strAiPickJhei == "Scissors":
        if strUserPickJhei == "Rock":
            intUserPointsJhei = intUserPointsJhei + 1
            strWinlossJhei = "Scissors. You Won!"
        elif strUserPickJhei == "Paper":
            intAiPointsJhei = intAiPointsJhei + 1
            strWinlossJhei = "Scissors. You lost!"

    listComparingValsJhei[0] = strUserPickJhei
    listComparingValsJhei[1] = intAiPointsJhei
    listComparingValsJhei[2] = intUserPointsJhei
    listComparingValsJhei[3] = strWinlossJhei

def defHardAIJhei(listComparingValsJhei):
    strAiPickJhei = str(random.choices(listWinTieLostTkes, listHardDifficultyTkes))
    defWinLossDifficultyJhei(strAiPickJhei, listComparingValsJhei)

def defWinLossDifficultyJhei(strAiPickJhei, listComparingValsJhei):
    strUserPickJhei = listComparingValsJhei[0]
    intAiPointsJhei = listComparingValsJhei[1]
    intUserPointsJhei = listComparingValsJhei[2]

    if "w" in strAiPickJhei:
        intUserPointsJhei = intUserPointsJhei + 1
        if strUserPickJhei == "Rock":
            strWinlossJhei = "Scissors. You won!"
        elif strUserPickJhei == "Paper":
            strWinlossJhei = "Rock. You won!"
        else:
            strWinlossJhei = "Paper. You won!"

    elif "t" in strAiPickJhei:
        strWinlossJhei = "It's a tie!"
    else:
        intAiPointsJhei = intAiPointsJhei + 1
        strWinlossJhei = "You lost!"
        if strUserPickJhei == "Rock":
            strWinlossJhei = "Paper. You lost!"
        elif strUserPickJhei == "Paper":
            strWinlossJhei = "Scissors. You lost!"
        else:
            strWinlossJhei = "Rock. You lost!"

    listComparingValsJhei[0] = strUserPickJhei
    listComparingValsJhei[1] = intAiPointsJhei
    listComparingValsJhei[2] = intUserPointsJhei
    listComparingValsJhei[3] = strWinlossJhei