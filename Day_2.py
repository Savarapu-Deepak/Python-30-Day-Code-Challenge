# Question: Write a program to iterate the first 10 numbers and in each iteration,
# print the sum of the current and previous number.

# Without Using Functions Concept.

for i in range(1, 11):
    print(i, " + ", (i - 1), " = ", (i + (i - 1)))

# With Using Functions Concept.

def result(n):
    for num in range(1, n + 1):
        print(num, ' + ', (num - 1), ' = ', (num + (num - 1)))
ran = int(input('Enter Range Value : '))
result(ran)