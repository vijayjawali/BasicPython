pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)

numbers = [2.3, 4.5, 6.7, 9.2, 1.6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

numbers.sort()
print(numbers)

missing_letter = sorted("The quick brown fox jumped over the lazy dog",
                        key = str.casefold)
print(missing_letter)

names = ["graham",
         "John",
         "terry",
         "eric",
         "terry",
         "michael"]

names.sort(key=str.casefold)
print(names)