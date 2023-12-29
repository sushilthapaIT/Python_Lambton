# num = [1,4,6,7,8,88,99,44]
# num = list(range(1,10,2))
# print(num)

'''2'''
# num = [1,2,3] * 3
# print(num)

'''3'''
# num = [1,2,3,4,5,6,7,8,9,10]
# for i in num:
#     print(i)

'''4'''
# num = [1,2,3,4,5,6,]
# num.insert(7,7)
# print(num[-1],num[-2],num[-3],num[-4],num[-5],num[-6],num[-7])


'''5'''
# my_list = [1,2,3,4,5,6,]
# index = 0
# while index < 6:
#  print(my_list[index])
#  index += 1


'''6'''
# num = [1,2,3,4,5,6,]
# print(len(num))


'''7'''
# num = [1,2,3,4,5,6,]
# num[0] = 99
# print(num)

# num = [0]*5
# index = 0
# while index < len(num):
#     num[index] = 99
#     index += 1
# print(num)


'''8'''
# numDays = 5
# def main():
#     sales = [0] * numDays
#     index = 0
#     print('Enter the sales for each day.')

#     while index < numDays:
#         print('Day #', index + 1,': ', sep='', end='')
#         sales[index] = float(input())
#         index = index + 1

#     print('Here are the values you entered:')
#     for value in sales:
#         print(value)

# main()


'''concatenate list'''
# boyName = ['ram', 'shyam', 'hari']
# girlName = ['sita', 'rita', 'gita']

# total = boyName + girlName

# boyName.append(girlName)
# print(total)

# one = [1,2,3,4,]
# two = [7,8,9,0]
# one = one + two
# one.pop(1)
# one.insert(1,12)
# print(one)


'''9'''

# days = ['sunday', 'monday','tuesday','wednesday','thursday','friday','saturday']

# for da in days:
# print(days[:])
# numbers = [1, 2, 3, 4, 5]
# my_list = numbers[1:]
# print(my_list)


# numbers = [1, 2, 3, 4, 5]
# my_list = numbers[:1]
# print(my_list)


# numbers = [1, 2, 3, 4, 5]
# my_list = numbers[-3:]
# print(my_list)

# def main():
#     days = ['sunday','tuesday','wednesday','friday','saturday']


#     user = input("Enter if your fav day is in list or nor?\n")

#     if user in days:
#         print("wow! your date is in list.")
#     else:
#         print("Ooops, not in the list")

# main()

# days = ['sunday', 'monday','tuesday','wednesday','thursday','friday','saturday']
# days.index(2)
# print(days)


# def main():
#     empty = []
#     again = 'y'

#     while again == 'y':
#         userInput = input("Enter name: ")

#         again = input("Do u want to try again? (y to continue)")
#     empty.append(userInput)
#     print(empty)

# main()


# def main():
#     menu = []
#     another = 'y'

#     while another == 'y':
#         mennu = input("Enter a food in new menu: ")

#         another = input("Do you want to add more:\npress y to continue: ")
#         menu.append(mennu)

#         rem = input("Do u want to remove any item? ")

#         print(menu)

# main()

# lis = ['momo', 'chhowmin', 'khayenge', 'nepal', 'me', 'rehe', 'jayenge']
# print(f"Here are the list of the food\n{lis}")
# rem = input("Which item should i change? ")

# try:
#     index = lis.index(rem)
#     new = input("Enter the new value: ")

#     lis[index] = new

#     print("New menu")
#     print(lis)
# except ValueError:
#     print("invalid input") 


'''INSERT'''
# name = ['ram', 'hari', 'rita']
# print(f"Name before Insert\n{name}")

# name.insert(2,'rose')
# print(f"Name after insert\n{name}")


'''SORT'''
# my_list = ['beta', 'alpha', 'delta', 'gamma']
# print(f"List before sort\n{my_list}")

# my_list.sort()
# print(f"List after sort\n{my_list}")


'''REMOVE'''
# def main():
#     food = ['pizza', 'burger', 'chips']

#     print(f"Here are the items of food in list.\n{food}")

#     item = input("Which item should I remove? ")
#     try:
#         food.remove(item)
#         print(f"New Menu\n{food}") 
#     except ValueError:
#         print("Invalid Input")

# main()


'''REVERSED'''
# food = ['pizza', 'burger', 'chips']
# print(f"before reserved\n{food}")
# food.reverse()
# print(f"after reserved\n{food}")


'''MEGAN RESTAURANT'''
# print("***************************")
# print("----------WELCOME-------------")
# print("***************************")

# def main():
#     lis = []
#     rate = 0
#     numEmployees = 6
#     for emp in range(numEmployees):
#         user = int(input(f"Enter the hours worked by employee {emp + 1}: "))
#         lis.append(user)

#     hour = float(input("Enter the hourly pay rate: "))
#     for i in lis:
#         rate = i * hour
#         print(f"Gross pay for employee {emp}: ${format(rate,'.2f')}")

# main()


'''TOTAL'''

# li = [1,2,3,4,5,6,7,8,]
# result = sum(li)
# print(result)


# def main():
#     # Create a list.
#     numbers = [2, 4, 6, 8, 10]

#     # Display the total of the list elements.
#     print('The total is', get_total(numbers))

# # The get_total function accepts a list as an
# # argument returns the total of the values in
# # the list.
# def get_total(value_list):
#     # Create a variable to use as an accumulator.
#     total = 0

#     # Calculate the total of the list elements.
#     for num in value_list:
#         total += num

#     # Return the total.
#     return total

# # Call the main function.
# main()
