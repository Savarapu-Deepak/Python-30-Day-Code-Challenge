# Question: Write a program to remove characters from a string starting
# from zero up to n and return a new string.

# Without Using Functions Concept.

data = input('Enter Any String Data : ')
n = int(input('Enter Character Number to be Start :  '))
if n < len(data):
    print(data[n : ])
else:
    print('n value Should be Lesser than String Value')
