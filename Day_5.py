# Question: Write a function to return True if the first and last number of a given list is same.
# If numbers are different then return False.

# Without Using Functions Concept.
data = eval(input('Enter List Data : '))
if data[0] == data[-1]:
    print('True')
else:
    print('False')

# Using Function Concept.

def result(data):
    if data[0] == data[-1]:
        return True
    else:
        return False
data_List = eval(input('Enter List Data : '))
res = result(data_List)
print(res)