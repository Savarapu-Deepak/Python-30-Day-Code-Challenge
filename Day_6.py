# Question: Iterate the given list of numbers and print only those numbers which are divisible by 5.

# Without Using Functions Concept.
data = eval(input('Enter List Data : '))
for num in data:
    if num % 5 == 0:
        print(num)

# With Using Functions Concept.

def result(list_data):
    for _ in list_data:
        if _ % 5 == 0:
            print(_)
data = eval(input('Enter List Data : '))
result(data)