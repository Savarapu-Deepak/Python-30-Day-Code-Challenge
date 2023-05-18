# Change Adds Program.....

def changeAdds(num):
    b = bin(num)
    b = b[2:]
    b1 = ''
    for i in b:
        if i == '1':
            b1 += '0'
        else:
            b1 += '1'
    else:
        print(b)
        print(b1)
    sum = 0
    for num in range(len(b1)):
        sum = sum + int(b1[num]) * (2 ** (len(b1) - (num + 1)))
    else:
        print(sum)


changeAdds(50)
