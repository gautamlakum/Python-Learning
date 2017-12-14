#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 23:44:29 2017

@author: LAKUM
"""

"""
Lists
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

