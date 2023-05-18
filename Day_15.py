# Python Program to reverse the given integer with a Space in between them.

data = int(input('Enter Any Number : '))
while data > 0:
    digit = data % 10
    data //= 10
    print(digit, end=' ')
