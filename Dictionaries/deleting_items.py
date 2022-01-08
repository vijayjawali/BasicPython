vehicles = {'dream': 'Honda 250T', 'er5': 'Kawasaki ER5', 'can-am': 'Bombardier Can-Am 250',
            'virago': 'Yamaha XV250', 'tenere': 'Yamaha XT650', 'jimny': 'Suzuki Jimny 1.5',
            'fiesta': 'Ford Fiesta Ghia 1.4', 'starfighter': "Lockheed F-104", 'learjet': "bombardier Learjet 75",
            'toy': "glider", 'roadster': 'triumph Street Triple'}

del vehicles['starfighter']
#del vehicles['f1']
result = vehicles.pop("f1", "You wish you had F1!")
print(result)

print()
plane = vehicles.pop("learjet")
print(plane)

print()
bike = vehicles.pop("tenere", "not present")
print(bike)

print()
for key, value in vehicles.items():
    print(key, value, sep=", ")
