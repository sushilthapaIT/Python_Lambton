#CSD-1233-01
#Assignment 9
#Sushil Thapa
#C0919991
#Dec 3, 2023

#Importing datetime
import re
from datetime import datetime


#Creating a function is_com_web()
def is_com_web(string):
    #Checking if the lowerchase string ends with '.com'
    return string.lower().endswith('.com')


#Creating a function is_yes()
def is_yes(s):
    #Checks if the argument is 'y' or 'Y', or it starts with 'yes'
    return s.lower() == 'y' or s.lower().startswith('yes')


#Creating a function sdrawkcab()
def sdrawkcab(s):
    #If it contains only letters and whitespace, return the reversed string
    if all(char.isalpha() or char.isspace() for char in s):
        return s[::-1]
    else:
        #If it contains other characters, return copy of the original string
        return s


#Creating a function total_digits()
def total_digits(s):
    #Checks it the string contains only numeric characters
    if s.isdigit():
        #If it contains only numeric characters, calculate and return the sum of all digits
        return sum(int(digit) for digit in s)
    else:
        #If it contains non numeric characters, return -1
        return -1


def convert_date(s):
    date_pattern = re.compile(r"^\d{2}/\d{2}/\d{4}$")
    if date_pattern.match(s):
        try:
            date_obj = datetime.strptime(s, "%m/%d/%Y")
            return date_obj.strftime("%B %d, %Y")
        except ValueError:
            pass
    return "InvalidDate"

