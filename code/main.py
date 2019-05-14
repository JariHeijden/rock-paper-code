#random for the AI, sys for closing when errors happen, time to delay certain things
import random, sys, time

rpsTupleJhei = ("Rock", "Paper", "Scissors")    #tuple for the AI to pick from
aiPickJhei = ""                                 #string so the AI can remember it's pick
roundAmountJhei = 0                             #round amount so you can play multiple rounds

#introduction of the program
print("Rock Paper Code", "This project was made by Jari van der Heijden, Thijs van Kessel and Amin Khachiche", "The function of this project", sep="\n")

userPickJhei = input("Pick: Rock, Paper or scissors?\n")

if "ro" in userPickJhei.lower():
    userPickJhei = "Rock"
elif "pa" in userPickJhei.lower():
    userPickJhei = "Paper"
elif "sc" in userPickJhei.lower():
    userPickJhei = "Scissors"
else:
    sys.exit("FATAL ERROR CLOSING NOW!")

aiPickJhei = random.choice(rpsTupleJhei)
print(userPickJhei)
print(aiPickJhei)

if aiPickJhei == userPickJhei:
    print("You both played", aiPickJhei, "it's a tie!")
if aiPickJhei == "Rock":
    if userPickJhei == "Paper":
        print("You covered his rock using paper!\nYou won!")
    elif userPickJhei == "Scissors":
        print("Your scissors got destroyed with a rock...\nYou lost")
if aiPickJhei == "Paper":
    if userPickJhei == "Scissors":
        print("You've cut his paper right in half!\nYou won!")
    elif userPickJhei == "Rock":
        print("Your rock got covered by a measly piece of paper...\nYou lost")
if aiPickJhei == "Scissors":
    if userPickJhei == "Rock":
        print("You obliterated his scissors!\nYou won!")
    elif userPickJhei == "Paper":
        print("Your paper got cut in half...\nYou lost")
