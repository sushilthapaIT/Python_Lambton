'''purchase = float(input('Enter how many books you purchased in a month: '))

if (purchase <= 0):
    print('you earned 0 point')
elif(purchase <=2):
    print('you earned 5 points')
elif(purchase <=4):
    print('you earned 15 points')
elif(purchase <=6):
    print('you earned 30 points')
else:
    if(purchase <= 8 or purchase > 8):
        print('you earned 60 points')'''


'''purchase = float(input('how many package you purchased'))
real = 99
disc = 0
total = 0 
if(purchase >=10 and purchase <= 19):
    disc = 10/100 * real
    total = purchase * real
    print(f'your dis amount is ', format(disc, '.2f'))
    print(f'your total is ',format(total, '.2f'))

elif(purchase >= 20 and purchase <= 49):
    disc = 20/100 * real
    total = purchase * real
    print(f'your disc amount is ',format(disc, '.2f'))
    print(f'your total is ',format(total , '.2f'))

elif(purchase >= 50 and purchase <= 99):
    disc = 30/100 * real
    total = purchase * real
    print(f'your disc amount is: ',format(disc, '.2f'))
    print(f'your total is: ',format(total , '.2f'))

else:
    if(purchase >= 100):
        disc = 40/100 * real
        total = purchase * real
        print(f'your disc amount is ', format(disc, '.2f'))
        print(f'your total is ',format(total , '.2f'))'''


'''purchase = float(input('how many package you purchased'))
real = 99
disc = 0
total = 0 

if (purchase >= 10 and purchase <=19):
    disc = 10/100
elif(purchase >=20 and purchase <=49):
    disc = 20/100
elif(purchase >=50 and purchase <=99):
    disc =  30/100
elif(purchase>=100):
    disc = 40/100

disc_amt = real * (1 - disc)
total = disc_amt * purchase

print(f"Discount: {disc_amt * 100}%")
print(f"Total amount after discount: ${total:.2f}")'''



'''package = float(input('enter the weight of package'))

if (package <= 2):
    charge = 1.50
elif(package <=6):
    charge =  3.00
elif(package <=10):
    charge = 4.00
else:
    charge = 4.75

    SHIP_CHARGE = package * charge

    print(f"your shipping charge is",SHIP_CHARGE)'''


pocket = float(input('enter pocket from 0-36: '))

if (pocket < 0 or pocket > 36):
    print('error!!')
elif(pocket == 0):
     print('green')
elif(pocket <= 1 or pocket <=10):
        if(pocket % 2 == 0):
            print('green')
        else:
            print('red')

elif(pocket <=11 or pocket <= 18):
        if(pocket % 2 == 0):
            print('red')
        else:
             print('green')