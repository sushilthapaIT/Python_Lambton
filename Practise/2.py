sum = 0

num = int(input('enter how many number sum u want to do?'))

for i in range(num):
    nub = int(input(f'Enter {i+1} times: '))

    sum = sum + nub

print('the sum of all number is:',sum)


'''for i in range(1,10,2):
    for j in range(1,10,2):
        print(i , j)
'''
