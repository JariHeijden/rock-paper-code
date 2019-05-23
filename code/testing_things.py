import time, random
listWinTieLostTkes = ["win", "tie", "loss"]
listEasyDifficultyTkes = [0.45, 0.30, 0.25]

while True:
    yeet = str(random.choices(listWinTieLostTkes, listEasyDifficultyTkes))
    time.sleep(0.5)
    print(yeet)
    