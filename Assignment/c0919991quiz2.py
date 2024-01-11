#CSD-1233-01
#Quiz 2
#Sushil Thapa
#C0919991
#Nov 24, 2023

#Defining a function named sort_str_int_float_list that takes a sequence as a parameter
def sort_str_int_float_list(sequence):
    #Initializing three empty lists to store elements of string, integer, and float types
    str_list = []   #Creating empty lists to store elements of string
    int_list = []   #Creating empty lists to store elements of integer
    float_list = [] #Creating empty lists to store elements of string

    #Looping through each element in the input sequence
    for element in sequence:
        #Checking if the element is of string type
        if isinstance(element, str):
            #Appending the string element to the str_list
            str_list.append(element)
        #Checking if the element is of integer type
        elif isinstance(element, int):
            #Appending the integer element to the int_list
            int_list.append(element)
        #Checking if the element is of float type
        elif isinstance(element, float):
            #Appending the float element to the float_list
            float_list.append(element)

    #Returning a two-dimensional list containing the three lists of string, integer, and float elements
    return [str_list, int_list, float_list]