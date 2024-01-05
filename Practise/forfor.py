for outer in range(1,11):
    for inner in range(1,11):
        print(inner * outer, end=' ')
    print()


for i in range(11,0,-1):
    for j in range(i):
        print("*" , end='')
    print()