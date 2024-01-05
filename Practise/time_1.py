import time

print("To know the remaining date of your birthday")
input("Press Enter to play")

while True:
    ur = input("Enter your birthday date in 'yyyy/mm/dd': ")
    if ur.isdigit():
        break
    else:
        print("Invalid Input!!")

today = time.time()