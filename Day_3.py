# Question: Write a program to accept a string from the user and display characters
# that are present at an even index number.

# Without Using Functions Concept.

data = input('Enter Any String : ')
for i in range(0, len(data), 2):
        print(i, data[i])

# With Using Functions Concept.

def result(string):
    for i in range(len(string)):
        if i % 2 == 0:
            print(i, string[i])
data = input('Enter Any String Data : ')
result(data)