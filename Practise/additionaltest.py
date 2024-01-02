
def add():
    while True:
        import random
        ing = random.randint(1,10)
        ni = random.randint(1,10)

        sum = ing + ni
        print(f"{ing} + {ni} = {sum}")
        user = input(f"Enter the sum of {ing} + {ni} = ")
        user = int(user)
        if user == sum:
            print("correct")
            break
        else:
            print("false")

add()