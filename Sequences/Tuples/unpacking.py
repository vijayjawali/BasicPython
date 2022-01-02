a = b = c = d = e = f = 12
print(c)

x, y, z = 1, 2, 76
print(x)
print(y)
print(z)

print("Unpacking a tuple")
data = 1, 2, 76
x, y, z = data
print(x)
print(y)
print(z)

print("Unpacking a list")
data_list = [12, 13, 14]
x, y, z = data_list
print(x)
print(y)
print(z)

print()
for t in enumerate("abcdefgh"):
    index, character = t
    print(index, character)


welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984


title, artist, year = metallica
print(title)
print(artist)
print(year)

table = ("Coffee table", 200, 100, 75, 34.50)
print(table[1] * table[2])
name, length, width, height, price = table
print(length * width)