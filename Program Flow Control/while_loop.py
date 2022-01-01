# for i in range(10):
#     print("i is now {}".format(i))

i =0
while i <10:
    print("i is now {}".format(i))
    i +=1

available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit.casefold() not in available_exits:
    chosen_exit = input("please choose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game over")
        break

else:
    print("aren't you glad you got out of there")

