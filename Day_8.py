# Desired Output:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6
# 7 7 7 7 7 7 7

for i in range(1, 8):
    for j in range(i):
        print(i, end=' ')
    print()