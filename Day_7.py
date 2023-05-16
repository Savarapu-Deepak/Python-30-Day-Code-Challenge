# Question: Write a program to find how many times substring “Emma” appears in the given string.

# Without Using Functions Concept.

data = input('Enter Any String : ')
check = input('Enter Sub String to be Find : ')
result = data.count(check)
print(result)

# Without Using String Method.
string_Data = input('Enter String Data : ')
data = input('Enter Sub String to be Count : ')
count, check = 0, string_Data.split()
for word in check:
    if word == data:
        count += 1
else:
    print(count)

# By Using Functions Concept.

def check(string_data, sub_String_Data):
    count, chek = 0, string_data.split()
    for word in chek:
        if word == sub_String_Data:
            count += 1
    else:
        print(count)
string_Data = input('Enter String Data : ')
sub_String_data = input('Enter Sub String Data : ')
check(string_Data, sub_String_data)