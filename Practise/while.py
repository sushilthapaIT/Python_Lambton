MAXBET = 5
MINBET = 1
# def amou():
#     while True:
#         user = input("Enter number: ")
#         if user.isdigit():
#             user = int(user)
#             if user > 0:
#                 break
#             else:
#                 print("Enter above 0")
#         else:
#             print("Invalid Input!!!!Enter num")
#     return user



def max():
    while True:
        inp = input(f"Enter number of bet 1 - {MAXBET}: ")
        if inp.isdigit():
            inp = int(inp)
            if inp <= MAXBET or inp >= MINBET: 
                break
            else:
                print("Enter between 1-5 only")
        else:
            print("Invalid Input!!Enter num")
    print(inp)
            
max()

# def main():
#     bal = amou()

# main()