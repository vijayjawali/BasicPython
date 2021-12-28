letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[::-1]
print(backwards)

# create a slice that produces the characters qpo
print(letters[16:13:-1])

# slice the string to produce edcba
print(letters[4::-1])

# slice the string to produce the last 8 characters in reverse order
print(letters[:25-8:-1])

print(letters[-4:])

print(letters[-1:])

print(letters[:1])

empty =""

print(empty[:1])  # use instead of print(empty[0]) to avoid error
