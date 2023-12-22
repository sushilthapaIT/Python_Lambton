# Function 1: add_two
def add_two(a, b): #Function definition for adding two values, 'a' and 'b'.
    if isinstance(a, (int, float)) and isinstance(b, (int, float)): #Checking if both 'a' and 'b' are either integers or floats.
        return a + b #Returning the sum of 'a' and 'b'.
    elif isinstance(a, (str, list, tuple)) and isinstance(b, (str, list, tuple)):  #Checking if both 'a' and 'b' are either strings, lists, or tuples.
        return a + b  #Returning the concatenation of 'a' and 'b'.
    else:
        raise ValueError("Unsupported types for add_two function") #Raising a ValueError if 'a' and 'b' have unsupported types.

# Function 2: seq_total
def seq_total(seq): #Function definition for calculating the total of a sequence, 'seq'.
    if all(isinstance(item, (int, float)) for item in seq): #Checking if all items in 'seq' are either integers or floats.
        return sum(seq) #Returning the sum of all elements in the sequence if they are numeric.
    elif all(isinstance(item, (str)) for item in seq): #Checking if all items in 'seq' are strings.
        return ''.join(seq) #Returning the concatenation of all elements in the sequence if they are strings.
    else:
        raise ValueError("Unsupported types in the sequence for seq_total function") #Raising a ValueError if 'seq' contains unsupported types.

# Function 3: seq_split
def seq_split(seq): #Function definition for splitting a sequence, 'seq', into two halves.
    length = len(seq) #Getting the length of the input sequence.
    split_index = length // 2 if length % 2 == 0 else length // 2 + 1 #Calculating the split index based on whether the length is even or odd.
    return [seq[:split_index], seq[split_index:]] #Returning a list containing two halves of the sequence based on the calculated split index.

# Function 4: safe_list_remove
def safe_list_remove(lst, element): #Function definition for safely removing an element from a list.
    if element in lst: #Checking if the specified element is present in the list.
        lst_copy = lst[:] #Creating a copy of the original list to avoid modifying it directly.
        lst_copy.remove(element) #Removing the specified element from the copied list.
        return lst_copy #Returning the modified copy of the list.
    else:
        return lst #Returning the original list unchanged if the element is not present.

# Function 5: seq_min_max
def seq_min_max(seq): #Function definition for finding the minimum and maximum values in a sequence, 'seq'.
    return min(seq), max(seq) #Returning a tuple containing the minimum and maximum values of the sequence.