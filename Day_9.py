# Question - Palindrome Check

# Without Using Function Concept.

data = int(input('Enter Any Number : '))
check = data
rev = 0
while data > 0:
    rem = data % 10
    rev = (rev * 10) + rem
    data //= 10
else:
    if check == rev:
        print(rev, 'is a Palindrome Number')
    else:
        print(rev, 'is not a Palindrome Number')

# 
