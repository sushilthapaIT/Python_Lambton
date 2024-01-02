def inp():
    user = input("Enter First Name: ")
    user2 = input("Enter Your Age: ")
    return user, user2


def gtr(user,user2):
    print("Your first name is:",user)
    print("Your age is:",user2)

def main():
    user, user2 = inp()
    gtr(user,user2)

main()