# Python Program to display words that are repeated more than or equal to n times in a given string.

data = input('Enter Any String Data : ')
check = int(input('Repeated Integer : '))
words = data.split()
new = {}
count = 0
for char in words:
    if char not in new.keys():
        new[char] = 1
    else:
        new[char] += 1
else:
    print(new)
    for i in new.keys():
        if check == new[i]:
            print(i, end = ' ')

