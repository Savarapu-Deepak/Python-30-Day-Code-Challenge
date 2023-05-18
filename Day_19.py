# Find the Maximum Product of Two Numbers in a List.

def check():
    data = eval(input('Enter List Data : '))
    length = len(data)
    if length < 2:
        print('No Pair Exists')
    else:
        max = data[0] * data[1]
        for i in range(len(data)):
            for j in range(i+1, len(data)):
                if (data[i] * data[j]) > max:
                    max = (data[i] * data[j])
        return (data[i], data[j], max)
print(check())
