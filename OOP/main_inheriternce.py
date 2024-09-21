from player import Player

tim = Player("Tim")

from enemy import Enemy, Troll, Vaampyre, VampyreKing

random_monster = Enemy("Basic enemy", 12, 1)
print(random_monster)


ugly_troll = Troll("Pug")
print("Ugly troll: {}".format(ugly_troll))

another_troll = Troll("Ug", 18, 1)
print("Another troll: {}".format(another_troll))

another_troll.take_damage(18)
print(another_troll)

brother = Troll("Urg", 23)
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

vamp = Vaampyre("Vlad")
print(vamp)

vamp.take_damage(5)
print(vamp)

while vamp.alive:
    if not vamp.dodges():
        vamp.take_damage(1)
        print(vamp)

dracula = VampyreKing("Dracula")
print(dracula)
dracula.take_damage(12)
print(dracula)
