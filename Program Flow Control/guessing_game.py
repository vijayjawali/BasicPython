import random

highest = 1000
answer = random.randint(1, highest)

guess = 0

while guess != answer:
    print("please guess a number between 1 and {}: ".format(highest))
    guess = int(input())
    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it.")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")