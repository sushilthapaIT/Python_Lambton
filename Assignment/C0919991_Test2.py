#Sushil Thapa
#C0919991
#Test 2
#Dec 14, 2023

#Function 1
#Creating Function divide_me
def divide_me(num1, num2):
#Checking if the denominator is zero to avoid division by zero error
    if num2 == 0:
        return "Error: Division by zero is undefined"

    #Calculating floating-point division, integer division, and remainder
    result_float = num1 / num2
    result_int = num1 // num2
    result_remainder = num1 % num2

    #Returning a list with the three results
    return [result_float, result_int, result_remainder]

#Function 2
#Creating Function format_currency
def format_currency(number):
    #Checking if the input is a valid number (integer or float)
    if not isinstance(number, (int, float)):
        return ""  #Returning an empty string for invalid input
    #Formatting the number with two decimal places and commas for thousands separator
    formatted_number = "{:,.2f}".format(round(number, 2))
    #Returning the formatted number as a string
    return formatted_number


#Function 3
#Creating Function validate_input
def validate_input(string, valid_strings):
    #Checking if all elements in the valid strings list are strings
    if not all(isinstance(s, str) for s in valid_strings):
        return False  #Returning False if any element in valid strings is not a string   
    #Checking if the lowercase version of the input string is in the lowercase version of valid strings
    return string.lower() in [s.lower() for s in valid_strings]


#Function 4
#Creating Function validate_password
def validate_password(password):
#Checking for password conditions: no spaces, minimum length 8, at least one uppercase letter, at least one lowercase letter, at least one digit, and no semicolon (;)
    if (
        any(c.isspace() for c in password)         #Check for spaces
        or len(password) < 8                       #Check for minimum length
        or not any(c.isupper() for c in password)  #Check for at least one uppercase letter
        or not any(c.islower() for c in password)  #Check for at least one lowercase letter
        or not any(c.isdigit() for c in password)  #Check for at least one digit
        or ';' in password                         #Check for semicolon presence
    ):
    #Return False if any condition is not met
        return False   
    #If all conditions are met, return True (password is valid)
    return True

#Function 5
#Creating Function morse_code
def morse_code(input_string):
    #Defining the set of valid characters for conversion
    valid_characters = set("abcdefghijklmnopqrstuvwxyz0123456789 ,.?")
    #Checking if all characters in the input string are valid
    if not all(char.lower() in valid_characters for char in input_string.lower()):
    #Returning an empty list if there are invalid characters
        return []  
    #Dictionary mapping characters to their Morse code representations
    morse_code_dict = {
        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
        'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
        'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
        's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
        'y': '-.--', 'z': '--..', '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.', ' ': ' ', ',': '--..--', '.': '.-.-.-',
        '?': '..--..'
    }
    #Creating a list of Morse code representations for each character in the input string
    morse_code_list = [morse_code_dict[char.lower()] for char in input_string.lower()]
    #Returning the list of Morse code representations
    return morse_code_list