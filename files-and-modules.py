#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 14:15:56 2017

@author: LAKUM
"""

"""
Tuples

Description:
    Tuples are used to store related pieces of information.
    For e.g. latitude and longitude
    Tuples are similar to the lists which store an ordered collection of objects
    which can be accessed by their indexes.
"""
place = (11.124674, 72.725183)      # Tuple having lat and long of a place
print(type(place))                  # Returns <class 'tuple'>
print(place[0])                     # Returns 11.124674

# Tuples can be used to assign multiple variables in a compact way
dimentions = 12, 10, 50
length, width, height = dimentions  # OR length, width, height = 12, 10, 50
print("The dimentions are {} x {} x {}".format(length, width, height))

# A dictionary with Tuples as their index and String as their value
locations = {(13.4125, 103.866667): "Angkor Wat",
             (25.73333, 32.6): "Ancient Thebes",
             (30.330556, 35.4433330): "Petra",
             (-13.116667, -72.583333): "Machu Picchu"}

def first_and_last(sequence):
    """Returns the first and last elements of a sequence"""
    return sequence[0], sequence[-1]

first_and_last(["Spam", "egg", "sausage", "Spam"])  # Returns a tuple

def hours2days(hours):
    """Returns how long is that period in days and hours"""
    days, hours = hours//24, hours%24
    return days, hours

print(hours2days(30))               # Returns (1, 6) where 1 is day(s), 6 is hours


"""
Default arguments in the functions
"""
def box(width, height, symbol='*'):
    """print a box made up of asterisks, or some other character.

        width: width of box in characters, must be at least 2
        height: height of box in lines, must be at least 2
        symbol: a single character string used to draw the box edges
    """
    print(symbol * width)           # print top edge of box

    # print sides of box
    for _ in range(height-2):
        print(symbol + " " * (width-2) + symbol) 

    print(symbol * width)           # print bottom edge of box
    
print(box(10, 10))                  # Prints a box with '*'
print(box(10, 10, '#'))             # Prints a box with '#'

def print_list(l, numbered=False, bullet_character='-'):
    """Prints a list on multiple lines, with numbers or bullets
    
    Arguments:
        l: The list to print
        numbered: set to True to print a numbered list
        bullet_character: The symbol placed before each list element. This is
                          ignored if numbered is True.
    """
    for index, element in enumerate(l):
        if numbered:
            print("{}: {}".format(index+1, element))
        else:
            print("{} {}".format(bullet_character, element))

print_list(["hello", "world", "universe"], False, '*')
print_list(["hello", "world", "universe"], True)
print_list(["hello", "world", "universe"])

def todo_list(new_task, base_list=['wake up']):
    """Returns a new list with a new task appeded
    
    Arguments:
        new_task: A new task to be appended
        base_list: A default task
    """
    base_list.append(new_task)
    return base_list

# Returns ['wake up', 'check the emails']
print(todo_list('check the emails'))

# Returns ['wake up', 'check the emails', 'meeting with the team'] because
# the list object is used each time the function is called. It isn't
# redefined each time it is called.
print(todo_list('meeting with the team'))

"""
Reading from a file
"""
f = open('sample.txt', 'r') # Opens the file in read-only mode
file_data = f.read()        # Reads the file data and creates a string object
f.close()                   # Closes the file
print(file_data)            # It will print the data from the sample.txt file

"""
Writing to a file
"""
f = open('sample.txt', 'w') # Opens the file in write mode
f.write('This is test 2')   # It deletes the old content and adds new
f.close()

"""
Append to a file
"""
f = open('sample.txt', 'a')     # Opens the file in the append mode
f.write(' This is test 3')      # It appends the new content to the old file
f.close()

"""
with

Description:
    It allows users to open a file, do operations on it, and close it automatically.
"""
with open('sample.txt', 'r') as f:
    file_data = f.read()
print(file_data)

"""
How to read
"""
with open('sample.txt') as f:
    print(f.read(2))    # Prints 'Th'
    print(f.read(5))    # Prints 'is is'
    print(f.read(6))    # Prints ' test '

# Create a list of lines from a file
line_list = []
with open('sample_new.txt') as file:        # This file has 2 lines of content in it
    for line in file:
        line_list.append(line.strip('\n'))  # Appends a line to the list
        
print(line_list)

def create_cast_list(file_name):
    """Returns a list of actors from the given file
    
    Arguments:
        file_name: the file name which needs to be read
    """
    cast_list = []
    with open(file_name) as file_data:
        for actor_data in file_data:
            actor = actor_data.split(',')
            cast_list.append(actor[0])
            
    return cast_list

print(create_cast_list('circus_cast_list.txt'))