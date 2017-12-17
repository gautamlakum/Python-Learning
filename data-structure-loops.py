#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 23:44:29 2017

@author: LAKUM
"""

"""
List

Desc: Lists are sortable, you can add an item to a list with 'append' and
list items are always indexed with numbers starting at 0.
"""
python_versions = [3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6]
print(python_versions[0])               # Prints 3.0 because index starts at 0
print(python_versions[4])               # Prints 3.4 which is at index 4
print(python_versions[-1])              # Prints 3.6 which is 1 index left to 0

# Slicing a list
sliced = python_versions[1:3]           # Slices from index 1 to 2, not 3
print(sliced)
sliced = python_versions[:3]            # Slices from index 0 to 2, not 3
print(sliced)
sliced = python_versions[2:]            # Slices from index 2 to the last one
print(sliced)

# Get the length of a list
print(len(python_versions))             # Prints 7, the number of elements in the list

# Get the max value
print(max(python_versions))             # Prints 3.6 which is the maximum value

string_list = ['a', 'bc', 'def', 'khi', 'ghij']
print(max(string_list))                 # Prints "khi", the maximum element in
                                        # a list of string is the element that
                                        # occurs last if the list is sorted
                                        # alphabatically. In our case, "khi"
                                        # would be last in the order.
                                        
# Get the min value
print(min(python_versions))             # Prints 3.0 which is the minimum value
print(min(string_list))                 # Prints "a", the minimum element

# Sorting
print(sorted(string_list))              # Returns a copy of the string_list list,
                                        # The original string_list remains unchanged
print(sorted(python_versions, reverse=True))    # Sorting in reverse order

# Joining a list
joined_list = "-".join(string_list)     # Joins each element with the "-"
print(joined_list)                      # Returns "a-bc-def-khi-ghij"
                                        
# Append to a list
string_list.append('lmno')              # Appends 'lmon' at the end of the list
print(string_list)                      # Returns ['a', 'bc', 'def', 'khi', 'ghij', 'lmno']

# Checks if an element is there in the List
if 'lmno' in string_list:               # Returns 'Yes'
    print('Yes')
else:
    print('No')


"""
Strings
"""
sample_string = "This is a string."
print(sample_string[5])                 # Prints "i" because index starts at 0

# Slicing a string
print(sample_string[5:7])               # Prints chars from index 5 upto 7, but not 7
print(sample_string[:4])                # Prints chars from index 0 upto 4, but not 4
print(sample_string[10:])               # Prints chars from index 10 to the last one

# Get the length of a list
print(len(sample_string))               # Prints 17, the length of the string


"""
for loop
"""
names = ['charlotte hippopotamus turner', 'oliver st. john-mollusc',
         'nigel incubator-jones', 'philip diplodocus mallory']
for name in names:                      # Prints all the strings from "names" var
    print(name)
    
"""
while loop
"""
cards = [7, 3, 4, 6, 9, 2, 10, 9, 4, 1]
hand = []

while sum(hand) <= 20:                  # Runs the loop till the sum is <= 10
    hand.append(cards.pop())
    
print(hand)

"""
Set

Desc: Sets are not ordered, so the order in which items appear can be
inconsistent and you add items to sets with 'add' function.
Like dictionaries and lists, sets are mutable.
You cannot have the same item twice and you cannot sort sets.
For these two properties a list would be more appropriate.
"""
countries = ['Angola', 'Maldives', 'India', 'United States', 'India']
print(len(countries))                   # It will print 5

country_set = set(countries)
print(len(country_set))                 # It will print 4 as it removes the
                                        # duplicate "India" entry and keeps only one

for country in country_set:             # Prints the country list
    print(country)                      # "India" will be printed only one time
    
print("India" in country_set)           # Checks if "India" is in the set, returns True

print("England" in country_set)         # Checks if "US" is in the set, returns False

# Add an element to the set
country_set.add("England")              # Adds "US" to the set
print("England" in country_set)         # Returns True

"""
Dictionary

Desc: Each item in a dictionary contains two parts: a key and a value,
the items in dictionary are not ordered.
Because dictionaries are not ordered they are not sortable,
and you do not add items to a dictionary with 'append' function.
"""
elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}
print(elements['hydrogen'])             # Prints 1, value of key 'hydrogen'

# Insert new values to the dictionary
elements['lithium'] = 3                 # Adds a new key 'lithium'
print(elements['lithium'])

# Checks if a key is there in the dictionary
if 'hydrogen' in elements:
    print('Yes')
else:
    print('No')
    
# Getting keys and values in a loop
for element in elements:
    print("{} - {}".format(element, elements[element]))
    
"""
Nested dictionary
"""
nested_elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}
print(nested_elements['hydrogen'])              # Prints the whole 'hydrogen' element
print(nested_elements['hydrogen']['weight'])    # Prints the weight of 'hydrogen'

# Add values to the new element in the nested dictionary
nested_elements['hydrogen']['noble_gas'] = False
nested_elements['helium']['noble_gas'] = True

######
monthly_takings = {'January': [54, 63], 'February': [64, 60], 'March': [63, 49],
                   'April': [57, 42], 'May': [55, 37], 'June': [34, 32],
                   'July': [69, 41, 32], 'August': [40, 61, 40], 'September': [51, 62],
                   'October': [34, 58, 45], 'November': [67, 44], 'December': [41, 58]}

def total_takings(yearly_record):
    total = 0
    for month in yearly_record.keys():  # .keys() gets dictionary view object
        total = total + sum(yearly_record[month])
    return total
        
print(total_takings(monthly_takings))