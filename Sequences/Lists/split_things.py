panagram = """The quick brown 
fox jumps\tover the lazy dog"""

words = panagram.split()
print(words)

numbers = "9,223,372,036,854,775,807"
print(numbers.split(","))

values_list = numbers.split(",")

integer_values = []
for value in values_list:
    integer_values.append(int(value))

print(integer_values)