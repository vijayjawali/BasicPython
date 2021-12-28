parrot = "Norwegian Blue"
print(parrot[0:6])  # Norweg => characters from 0 to 5 are printed excluding 6
print(parrot[3:5])
print(parrot[0:9])  # Norwegian
print(parrot[:9])  # Norwegian

print(parrot[10:14])  # Blue
print(parrot[10:])  # Blue

print(parrot[:6])
print(parrot[6:])

print(parrot[:6] + parrot[6:])

print(parrot[:])

print()
print(parrot[-4:-2])  # Bl
print(parrot[-4:12])  # Bl

# Using step in a slice
print()
print(parrot[0:6:2])  # Nre
print(parrot[0:6:3])  # Nw

number = "9,223;372:036 978,643,837;243"

seperators = number[1::4]

print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])