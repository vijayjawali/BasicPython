import random


def get_integer(prompt):
    """
    Get an integer from standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.

    :param prompt: the string that the user will see, when
        they're prompted to enter the value
    :return: the integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        print("{0} is not a valid number".format(temp))


print(input.__doc__)
print("*" * 80)
print(get_integer.__doc__)
print("*" * 80)

help(get_integer)

highest = 1000
answer = random.randint(1, highest)
print(answer)
guess = 0

while guess != answer:
    print("please guess a number between 1 and {}: ".format(highest))
    guess = get_integer(": ")
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
