# print(dir())

# for funcs in (dir(__builtins__)):
#     print(funcs)

import shelve

# print(dir())
# print()
# print(dir(shelve))

for obj in dir(shelve.Shelf):
    if obj[0] != '_':
        print(obj)
