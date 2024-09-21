class Wing:

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print('Flying')
        elif self.ratio == 1:
            print('Gliding')
        else:
            print('Running')


class Duck:

    def __init__(self):
        self._wing = Wing(1.8)

    def quack(self):
        print('Quack!')

    def walk(self):
        print('Walks like a duck.')

    def bark(self):
        print('The duck cannot bark.')

    def fly(self):
        self._wing.fly()


class Penguin:

    def quack(self):
        print('The penguin cannot quack.')

    def walk(self):
        print('Walks like a penguin.')

    def bark(self):
        print('The penguin cannot bark.')


def test_duck(duck):
    duck.quack()
    duck.walk()
    duck.bark()


if __name__ == "__main__":
    donald = Duck()
    donald.fly()