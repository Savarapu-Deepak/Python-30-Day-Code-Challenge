# Question: Given two integer numbers, return their product only if the product is equal
# to or lower than 1000; else, return their sum.

# Without Using Functions Concept.

x = int(input('Enter Number_1 : '))
y = int(input('Enter Number_2 : '))
if (x * y) <= 1000:
    print('Product or {} and {} is {}'.format(x, y, (x * y)))
else:
    print('Sum of {} and {} is {}'.format(x, y, (x + y)))

# With Using Functions Concept.

def result(num_1, num_2):
    if (num_1 * num_2) <= 1000:
        print(f'Product of {num_1} and {num_2} is {num_1 * num_2}')
    else:
        print(f'Sum of {num_1} and {num_2} is {num_1 + num_2}')
a = int(input('Enter Number_1 : '))
b = int(input('Enter NUmber_2 : '))
result(a, b)