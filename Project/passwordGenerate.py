import random

print(f"----------------------\nWelcome to password Generator\n---------------------------")
print()

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+<>?0123456789'
number = input("Amount of password to generate: ")
number = int(number)
length = input("Length of password to generate: ")
length = int(length)

print('\nHere are your password:')
for password in range(number):
    pwd = ''
    for c in range(length):
        pwd = pwd + random.choice(chars)
    print(pwd)