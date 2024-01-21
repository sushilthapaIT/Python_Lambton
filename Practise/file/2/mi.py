'''def main():
    name1 = input("Enter 1st name: ")
    name2 = input("Enter 2nd name: ")
    name3 = input("Enter 3rd name: ")

    myfile = open('friends.html' ,'a')

    myfile.write("<html>\n")
    myfile.write(name1 + '\n')
    myfile.write(name2 + '\n')
    myfile.write(name3 + '\n')
    myfile.write("I am new code")
    myfile.write("</html>")

    myfile.close()
    print('The names were written to new file called friends.txt successfully.')

main()'''



'''myfile = open('friends.txt', 'r')
content = myfile.read()
myfile.close()

# Print the content, not the file object
print(content)'''


f = open("film.txt", 'w')

userInput = int(input("Enter the running times for each videos: "))
print("Enter the running times for each video.")

count = 0
for i in range(userInput):
    vid = float(input(f"Video #{i+1} \n"))
    print(vid)
    count = count + 1
print(count, "ok")
f.close()



