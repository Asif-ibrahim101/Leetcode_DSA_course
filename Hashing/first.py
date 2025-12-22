#A hash function is a function that takes an input and deterministically converts it to an integer that is less than a fixed size set by the programmer. 
# Inputs are called keys and the same input will always be converted to the same integer.

#A set is another data structure that is very similar to a hash table. 
# It uses the same mechanism for hashing keys into integers. The difference between a set and hash table is that sets do not map their keys to anything. 
# Sets are more convenient to use when you only care about checking if elements exist. 
# You can add, remove, and check if an element exists in a set all in 

#An important thing to note about sets is that they don't track frequency. 
# If you have a set and add the same element 100 times, the first operation adds it and the next 99 do nothing.

#----------------------------------------------------------
#some important interface
# Declaration: a hash map is declared like any other variable. The syntax is {}
#hash_map = {}

# If you want to initialize it with some key value pairs, use the following syntax:
#hash_map = {1: 2, 5: 3, 7: 2}

# Checking if a key exists: simply use the `in` keyword
#1 in hash_map # True
#9 in hash_map # False

# Accessing a value given a key: use square brackets, similar to an array.
#hash_map[5] # 3

# Adding or updating a key: use square brackets, similar to an array.
# If the key already exists, the value will be updated
#hash_map[5] = 6

# If the key doesn't exist yet, the key value pair will be inserted
#hash_map[9] = 15

# Deleting a key: use the del keyword. Key must exist or you will get an error.
#del hash_map[9]

# Get size
#len(hash_map) # 3

# Get keys: use .keys(). You can iterate over this using a for loop.
#keys = hash_map.keys()
#for key in keys:
    #print(key)

# Get values: use .values(). You can iterate over this using a for loop.
#values = hash_map.values()
#for val in values:
    #print(val)
