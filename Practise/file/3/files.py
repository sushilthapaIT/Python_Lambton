def main():
    name = input("Enter a name: ")
    desc = input("Describe yourself: ")

    f = open('index.html', 'w')

    f.write("<html>")
    f.write("<head>")
    f.write("</head>")
    f.write("<body>")
    f.write("<center>")
    f.write("<h1>")
    f.write(name)
    f.write("</h1>")
    f.write("/center")
    f.write("<hr/>")
    f.write(desc)
    f.write("<hr/>")
    f.write("</body>")
    f.write("</html>")


    f.close()
    print("Written Successfully!!")

main()
