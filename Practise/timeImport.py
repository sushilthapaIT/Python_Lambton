# import random


# min = 1
# max = 10

# calc = ["*","-","+"]


import time

start = time.time()

input("Press anything to start!!")


while True:
    a = input("Enter number: ")
    if a.isdigit():
        print("good to go")
        break
    else:
        print("Try Again!")


end = time.time()
total = end - start
print(f"Completed in {format(total, '.2f')} seconds")