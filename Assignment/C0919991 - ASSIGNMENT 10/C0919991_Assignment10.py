#CSD 1233-01
#Assignment 10
#Sushil Thapa
#C0919991
#December 14, 2023

#Function to add an element to a dictionary
def dict_add_element(dictionary, key, value):
#Assigning the given value to the specified key in the dictionary
    dictionary[key] = value
#Returning the updated dictionary after adding the new key-value pair
    return dictionary


#Function to get the value corresponding to a key in a dictionary
def dict_get(dictionary, key):
#Checking if the key exists in the dictionary
    if key in dictionary:  
#Returning the value associated with the key if it exists
        return dictionary[key]  
    else:
#Returning a message if the key is not found in the dictionary
        return f"Value {key} not found"  

#Function to change a key in a dictionary
def dict_change_key(dictionary, existing_key, new_key):
#Checking if the existing key is present in the dictionary
    if existing_key in dictionary:  
            dictionary[new_key] = dictionary.pop(existing_key)
#Returning the updated dictionary after changing the key
    return dictionary 


#Function to pop a random key-value pair from a dictionary
import random
def dict_pop_item(dictionary):
    dict_copy = dictionary.copy()
    #Checking if the dictionary is not empty
    if dictionary:
        #Choosing a random key from the dictionary
        key = random.choice(list(dictionary.keys()))       
        #Creating a tuple with the popped key-value pair
        popped_item = (key, dictionary[key])        
        #Removing the key-value pair from the dictionary
        del dict_copy[key]        
        #Returning a list with the updated dictionary as the first element and the popped item as the second element
        return [dict_copy, popped_item[0]]
    else:
        #If the dictionary is empty, return the original dictionary and None as the popped item
        return [dictionary, None]

#Function to convert keys to lowercase in a dictionary
def dict_lower(dictionary):
#Creating a new dictionary with lowercase keys for string keys and the same keys for non-string keys
    lowercase_dict = {str(key).lower(): value for key, value in dictionary.items() if isinstance(key, str)}
    #Update the new dictionary with the keys and values for non-string keys
    lowercase_dict.update({key: value for key, value in dictionary.items() if not isinstance(key, str)})
    return lowercase_dict  #Returning the new dictionary with all keys converted to lowercase for string keys