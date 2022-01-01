if 0:
    print("true")
else:
    print("False")

name = input("Please enter your name: ")

# if name:
if name != "":
    print("hello, {}".format(name))
else:
    print("are you a man with no name")