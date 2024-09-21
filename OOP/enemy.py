class Enemy(object):
    def __init__(self, name="Enemy", lives=1, hit_points=0):
        self._name = name
        self._lives = lives
        self._hit_points = hit_points
        self._alive = True

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print("I took {} points damage and have {} left".format(damage, self._hit_points))
        else:
            self._lives -= 1
            if self._lives > 0:
                print("{0._name} lost a life".format(self))
            else:
                print("{0._name} is dead".format(self))
                self._alive = False

    def __str__(self):
        return "Name: {0._name}, Lives: {0._lives}, Hit points: {0._hit_points}".format(self)

    @property
    def alive(self):
        return self._alive


class Troll(Enemy):

    def __init__(self, name, lives=1, hit_points=23):
        super(Troll, self).__init__(name=name, lives=lives, hit_points=hit_points)

    def grunt(self):
        print("Me {0._name}. {0._name} stomp you".format(self))


class Vaampyre(Enemy):
    def __init__(self, name="Vaampyre", lives=3, hit_points=12):
        super(Vaampyre, self).__init__(name=name, lives=lives, hit_points=hit_points)

    def dodges(self):
        import random
        if random.randint(1, 3) == 3:
            print("***** {0._name} dodges *****".format(self))
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super(Vaampyre, self).take_damage(damage=damage)

    def __str__(self):
        return "Name: {0._name}, Lives: {0._lives}, Hit points: {0._hit_points}".format(self)


class VampyreKing(Vaampyre):
    def __init__(self, name):
        super(VampyreKing, self).__init__(name=name, lives=3, hit_points=140)

    def take_damage(self, damage):
        super(VampyreKing, self).take_damage(damage // 4)

    def __str__(self):
        return "Name: {0._name}, Lives: {0._lives}, Hit points: {0._hit_points}".format(self)