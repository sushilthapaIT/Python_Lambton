



f_name = input('what is your full name?')

c_num = input('What is your college id?')

csd_1 = float(input('What is your grade of CSD-1113?'))

csd_2 = float(input('What is your grade of CSD-1133?'))

csd_3 = float(input('What is your grade of CSD-1233?'))

csd_4 = float(input('What is your grade of CSD-2206?'))

csd_5 = float(input('What is your grade of CSD-3424?'))

csd_6 = float(csd_1 * 3);

csd_7 = float(csd_2 * 3);

csd_8 = float(csd_3 * 3);

csd_9 = float(csd_4 * 6);

csd_10 = float(csd_5 * 3);

sum = float(csd_6 + csd_7 + csd_8 + csd_9 + csd_10);

credit = float(3 + 3 + 3 + 6 + 3);

average = float(sum / credit);


print('Name: ' +f_name)
print('C Number: ' +c_num)
print()
print('CSD-1113: ',csd_6)
print('CSD-1133: ', csd_7)
print('CSD-1233: ', csd_8)
print('CSD-2206: ', csd_9)
print('CSD-3423: ', csd_10)
print()
print('Total Sum =', sum)
print('Total Credit Earned: ', credit)
print('Average = ',average)



