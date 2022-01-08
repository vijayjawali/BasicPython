vehicles = {'dream': 'Honda 250T', 'roadster': 'BMW R1100', 'er5': 'Kawasaki ER5', 'can-am': 'Bombardier Can-Am 250',
            'virago': 'Yamaha XV250', 'tenere': 'Yamaha XT650', 'jimny': 'Suzuki Jimny 1.5',
            'fiesta': 'Ford Fiesta Ghia 1.4', 'starfighter': "Lockheed F-104", 'learjet': "bombardier Learjet 75",
            'toy': "glider", 'roadster': 'triumph Street Triple'}

vehicles['virago'] = "yamaha XV535"

print()
for key, value in vehicles.items():
    print(key, value, sep=", ")