#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 23:27:49 2017

Description:
    Importing modules, its functions, methods.

@author: LAKUM
"""
"""
Importing modules
"""
# Import math module
import math
# Import datetime module
import datetime

print(math.factorial(5))    # Prints factorial

print(math.pow(2, 3))       # Prints 2 raised to power 3

print(math.exp(3))          # Returns e**3

print(datetime.datetime.now())  # Returns current date time

# Import a specific function or class from a module
from collections import defaultdict

# Import multiple functions or classes or objects from a module
from collections import abstractmethod, defaultdict

# Import a module and give it a name (usually a shorter one)
import datetime as dt
print(dt.datetime.now())

# Import an individual item from a module and give it a name
from csv import reader as csvreader

# NEVER USER THIS. It imports all the functions/objects and they all have
# their own names. Some of them may get overwritten.
# from random import *

# Import submodule
import os.path

# You can not import a function from a submodule
import os.path.isdir

# This is an example. It reads words from a file and generates a password
# by combining random 3 words.
import random as rd

word_file = "words.txt"
word_list = []

# Fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# Remove white space and make everything lowercase
		word = line.strip().lower()
		# Don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

def generate_password():
    password = rd.choice(word_list) + rd.choice(word_list) + rd.choice(word_list)
    return password

print(generate_password())
