# jabber = open("sample.txt",'r')
# for line in jabber:
#     print(line, end='')
# jabber.close()

# Reading line based on condition
# jabber = open("sample.txt",'r')
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end='')
# jabber.close()

# No need to close file
# with open("sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

# with open("sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

# .readlines reads entire file as a list
# with open("sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(type(lines))
#
# for line in lines:
#     print(line, end='')

# with open("sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines[::-1]:
#     print(line, end='')

# Reads file for end to start
# with open("sample.txt", 'r') as jabber:
#     lines = jabber.read()
#
# for line in lines[::-1]:
#     print(line, end='')
