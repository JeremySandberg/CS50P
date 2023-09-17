import random

while True:
    level = input("Level: ")
    if level.isnumeric():
        level = int(level)
        if level == 0: continue
        rng = random.randint(1, level)
        break

while True:
    guess = input("Guess: ")
    if guess.isnumeric():
        guess = int(guess)

        if level < guess or guess == 0:
            continue
        elif guess == rng:
            print("Just right!")
            break
        elif guess < rng:
            print("Too small!")
        elif guess > rng:
            print("Too large!")
