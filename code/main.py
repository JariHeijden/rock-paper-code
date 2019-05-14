import random, sys, time

rpsTupleJhei = ("Rock", "Paper", "Scissors")
aiPickJhei = ""


print("Rock Paper Code", "This project was made by Jari van der Heijden, Thijs van Kessel and Amin Khachiche", "The function of this project", sep="\n")

userPickJhei = input("Pick: Rock, Paper or scissors?\n")

if "k" in userPickJhei.lower():
    userPickJhei = "Rock"
elif "p" in userPickJhei.lower():
    userPickJhei = "Paper"
elif "s" in userPickJhei.lower():
    userPickJhei = "Scissors"
else:
    sys.exit("FATAL ERROR CLOSING NOW!")

aiPickJhei = random.choice(rpsTupleJhei)
print(aiPickJhei)

if aiPickJhei == userPickJhei:
    print("You both played", aiPickJhei, "Tie!")
if aiPickJhei == "Rock":
    if userPickJhei == "Paper":
        print("You covered the rock using paper \nYou won!")
    elif userPickJhei == "Scissors":
        print("Your scissors got destroyed with a rock...\nYou lost")
if aiPickJhei == "Paper":
    if userPickJhei == "Scissors":
        ("You've snipped his paper right in half!\nYou won!")
    elif userPickJhei == "Rock":
        ("Your rock didn't have affect on his paper...\nYou lost")
if aiPickJhei == "Scissors":
    if userPickJhei == "Rock":
        print("You obliterated his scissors\nYou won!")
    elif userPickJhei == "Paper":
        print("Your paper got cut in half...\nYou lost")