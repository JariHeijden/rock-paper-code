import time, random
from playsound import playsound
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
    #tie
    if strAiPickJhei == strUserPickJhei:
        print("You both played", strAiPickJhei, "it's a tie!")
        #code for Rock
    if strAiPickJhei == "Rock":
        if strUserPickJhei == "Paper":
            print("You covered his rock using paper!\nYou won!")
            playsound('C:/Users/Thijs/Documents/Git/rock-paper-code/sound/Point.wav')
            intUserPointsJhei = intUserPointsJhei + 1
        elif strUserPickJhei == "Scissors":
            print("Your scissors got destroyed with a rock...\nYou lost")
            playsound('C:/Users/Thijs/Documents/Git/rock-paper-code/sound/Wrong.wav')
            intAiPointsJhei = intAiPointsJhei + 1
        #code for Paper
    if strAiPickJhei == "Paper":
        if strUserPickJhei == "Scissors":
            print("You've cut his paper right in half!\nYou won!")
            playsound('C:/Users/Thijs/Documents/Git/rock-paper-code/sound/Point.wav')
            intUserPointsJhei = intUserPointsJhei + 1
        elif strUserPickJhei == "Rock":
            print("Your rock got covered by a measly piece of paper...\nYou lost")
            playsound('C:/Users/Thijs/Documents/Git/rock-paper-code/sound/Wrong.wav')
            intAiPointsJhei = intAiPointsJhei + 1
        #code for Scissors
    if strAiPickJhei == "Scissors":
        if strUserPickJhei == "Rock":
            print("You obliterated his scissors!\nYou won!")
            playsound('C:/Users/Thijs/Documents/Git/rock-paper-code/sound/Point.wav')
            intUserPointsJhei = intUserPointsJhei + 1
        elif strUserPickJhei == "Paper":
            print("Your paper got cut in half...\nYou lost")
            playsound('C:/Users/Thijs/Documents/Git/rock-paper-code/sound/Wrong.wav')
            intAiPointsJhei = intAiPointsJhei + 1
    time.sleep(1)
    print("\nYour score is: ", intUserPointsJhei, "\nThe AI score is: ", intAiPointsJhei, "\n")
    #everything below this is a soft reset so you start again in this while loop
    strAiPickJhei = ""
    strUserPickJhei = ""
    time.sleep(0.5)
    listComparingValsJhei[0] = strUserPickJhei
    listComparingValsJhei[1] = intAiPointsJhei
    listComparingValsJhei[2] = intUserPointsJhei
    #stops here

def defHardAIJhei(listComparingValsJhei):
    strAiPickJhei = str(random.choices(listWinTieLostTkes, listHardDifficultyTkes))
    defWinLossDifficultyJhei(strAiPickJhei, listComparingValsJhei)

def defWinLossDifficultyJhei(strAiPickJhei, listComparingValsJhei):
    strUserPickJhei = listComparingValsJhei[0]
    intAiPointsJhei = listComparingValsJhei[1]
    intUserPointsJhei = listComparingValsJhei[2]

    if "w" in strAiPickJhei:
        if strUserPickJhei == "Rock":
            print("You obliterated his scissors!\nYou won!")
            playsound('C:/Users/Thijs/Documents/Git/rock-paper-code/sound/Point.wav')
            intUserPointsJhei = intUserPointsJhei + 1
        elif strUserPickJhei == "Paper":
            print("You covered his rock using paper!\nYou won!")
            playsound('C:/Users/Thijs/Documents/Git/rock-paper-code/sound/Point.wav')
            intUserPointsJhei = intUserPointsJhei + 1
        else:
            print("You've cut his paper right in half!\nYou won!")
            playsound('C:/Users/Thijs/Documents/Git/rock-paper-code/sound/Point.wav')
            intUserPointsJhei = intUserPointsJhei + 1
    elif "t" in strAiPickJhei:
        print("You both played", strUserPickJhei, "it's a tie!")
    else:
        if strUserPickJhei == "Rock":
            print("Your rock got covered by a measly piece of paper...\nYou lost")
            playsound('C:/Users/Thijs/Documents/Git/rock-paper-code/sound/Wrong.wav')
            intAiPointsJhei = intAiPointsJhei + 1
        elif strUserPickJhei == "Paper":
            print("Your paper got cut in half...\nYou lost")
            playsound('C:/Users/Thijs/Documents/Git/rock-paper-code/sound/Wrong.wav')
            intAiPointsJhei = intAiPointsJhei + 1
        else:
            print("Your scissors got destroyed with a rock...\nYou lost")
            playsound('C:/Users/Thijs/Documents/Git/rock-paper-code/sound/Wrong.wav')
            intAiPointsJhei = intAiPointsJhei + 1

    time.sleep(1)
    print("\nYour score is: ", intUserPointsJhei, "\nThe AI score is: ", intAiPointsJhei, "\n")
    #everything below this is a soft reset so you start again in this while loop
    strAiPickJhei = ""
    strUserPickJhei = ""
    time.sleep(0.5)
    listComparingValsJhei[0] = strUserPickJhei
    listComparingValsJhei[1] = intAiPointsJhei
    listComparingValsJhei[2] = intUserPointsJhei