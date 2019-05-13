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
print(userPickJhei)
print(aiPickJhei)

if aiPickJhei == userPickJhei:
    print("Tie!")
if aiPickJhei == "Rock"