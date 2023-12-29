user = "y"
name =[]

while user == "y":
    en = input("Enter name: \n")

    name.append(en)
    user = input("Do you want to try again? [y/n] \n")

for nam in name:
    print(nam)