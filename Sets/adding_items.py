numbers = set()
print(numbers, type(numbers))

# numbers.add(1)
# print(numbers)

while len(numbers) < 4:
    next_value = int(input("please enter your next value: "))
    numbers.add(next_value)

print(numbers)