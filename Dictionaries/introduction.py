vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
}

print()
my_car = vehicles['fiesta']
print(my_car)

print()
commuter = vehicles['virago']
print(commuter)

print()
learner = vehicles.get("er5")
print(learner)

print()
print("keys are case sensitive")
learner = vehicles.get("ER5")
print(learner)