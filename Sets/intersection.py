from primes_and_squares import squares_generator, primes_generator

evens = set(range(0, 50, 2))
odds = set(range(1, 50, 2))

print(evens)
print(odds)

primes = set(primes_generator(100))
print(primes)

squares = set(squares_generator(100))
print(squares)

print(odds.intersection(squares))
print(odds & squares)

print(evens & squares)
print(evens.intersection(squares))

print()
trial_1 = {"Bob", "Charley", "Georgia", "John"}
trial_2 = {"Anne", "Charley", "Eddie", "Georgia"}

check_set = trial_1.intersection(trial_2)
print(check_set)

farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}
potential_rides = {"donkey", "horse", "camel"}

intersection = farm_animals & wild_animals & potential_rides
print(intersection)

mounts = farm_animals.intersection(wild_animals, potential_rides)
print(mounts)
