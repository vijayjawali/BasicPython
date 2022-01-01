name = input("Please enter your name: ")
age = int(input("How old are you {0}? ".format(name)))
print(age)

if age < 18:
    print("Please come back in {0} years.".format(18 - age))
elif age == 18:
    print("Welcome to voting for the first time")
else:
    print("You are old enough to vote")
    print("Please put an X in the box")