# Python Program to sort characters and numbers , so than 1st alphabets and then numbers are printed.


data_1 = 'A7B1R3'
nums, alphas = [], []
for char in data_1:
    if char.isdigit():
        nums.append(char)
    else:
        alphas.append(char)
result = sorted(alphas) + sorted(nums)
output = ''.join(result)
print(output)
