
class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle(make="kenwood", price=8.99)
print(kenwood.power_source)

print(Kettle.__dict__)
print(kenwood.__dict__)

# switch to power source atomic
Kettle.power_source = "atomic"


print(Kettle.__dict__)
print(kenwood.__dict__)
print(kenwood.power_source)

hamilton = Kettle(make="hamilton", price=8.99)
print(hamilton.power_source)

print(Kettle.__dict__)
print(hamilton.__dict__)

# switch to power source gas
hamilton.power_source = "gas"
print(hamilton.power_source)

print(Kettle.__dict__)
print(hamilton.__dict__)