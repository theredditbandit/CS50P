import random

while True: # this while loop handles getting input
    try:
        level = int(input("Level: "))
    except ValueError:
        pass
    else:
        if level >=1:
            break
        else:
            continue

gameint = random.randint(1,level)
# print(gameint) # for debugging

while True: # This while loop handles the Guessing part
    try:
        guess = int(input("Guess: "))
    except ValueError:
        pass
    else:
        if guess == gameint:
            print("Just right!")
            break
        elif guess < gameint:
            print("Too small!")
        elif guess > gameint:
            print("Too large!")
        elif guess <= 0:
            continue
