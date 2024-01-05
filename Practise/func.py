input("Press Enter to play! ")

def inp():
    start = int(input("Multiplication of which number: "))
    upto = int(input("Upto which number: "))
    return start, upto

def mul():
    start, upto = inp()
    for i in range(1, upto + 1):
        print(f"{start} * {i} = {start * i}")

mul()