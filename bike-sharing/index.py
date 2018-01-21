#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 17:49:58 2017

@author: LAKUM
"""

# Import necessary libraries
import csv
from datetime import datetime
from pprint import pprint

def print_first_point(filename):
    """
    This function prints and returns the first data point (second row) from
    a csv file that includes a header row.
    """
    # print city name for reference
    city = filename.split('-')[0].split('/')[-1]
    print('\nCity: {}'.format(city))
    
    with open(filename, 'r') as f_in:
        ## TODO: Use the csv library to set up a DictReader object. ##
        ## see https://docs.python.org/3/library/csv.html           ##
        trip_reader = csv.DictReader(f_in)
        
        ## TODO: Use a function on the DictReader object to read the     ##
        ## first trip from the data file and store it in a variable.     ##
        ## see https://docs.python.org/3/library/csv.html#reader-objects ##
        first_trip = trip_reader.__next__()
        
        ## TODO: Use the pprint library to print the first trip. ##
        ## see https://docs.python.org/3/library/pprint.html     ##
        pprint(first_trip)
        
    # output city name and first trip for later testing
    return (city, first_trip)

# list of files for each city
data_files = ['./data/NYC-CitiBike-2016.csv',
              './data/Chicago-Divvy-2016.csv',
              './data/Washington-CapitalBikeshare-2016.csv',]

# print the first trip from each file, store in dictionary
example_trips = {}
for data_file in data_files:
    city, first_trip = print_first_point(data_file)
    example_trips[city] = first_trip

def duration_in_mins(datum, city):
    """
    Takes as input a dictionary containing info about a single trip (datum) and
    its origin city (city) and returns the trip duration in units of minutes.
    
    Remember that Washington is in terms of milliseconds while Chicago and NYC
    are in terms of seconds. 
    
    HINT: The csv module reads in all of the data as strings, including numeric
    values. You will need a function to convert the strings into an appropriate
    numeric type when making your transformations.
    see https://docs.python.org/3/library/functions.html
    """
    if city == 'NYC' or city == 'Chicago':
        duration = int(datum['tripduration'])/60
    else:
        duration = int(datum['Duration (ms)'])/60000
    
    return duration


# Some tests to check that your code works. There should be no output if all of
# the assertions pass. The `example_trips` dictionary was obtained from when
# you printed the first trip from each of the original data files.
tests = {'NYC': 13.9833,
         'Chicago': 15.4333,
         'Washington': 7.1231}

for city in tests:
    assert abs(duration_in_mins(example_trips[city], city) - tests[city]) < .001
    
def time_of_trip(datum, city):
    """
    Takes as input a dictionary containing info about a single trip (datum) and
    its origin city (city) and returns the month, hour, and day of the week in
    which the trip was made.
    
    Remember that NYC includes seconds, while Washington and Chicago do not.
    
    HINT: You should use the datetime module to parse the original date
    strings into a format that is useful for extracting the desired information.
    see https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    """
    if city == 'NYC':
        ridetime = datum['starttime']
        date = datetime.strptime(ridetime, '%m/%d/%Y %H:%M:%S')
    elif city == 'Chicago':
        ridetime = datum['starttime']
        date = datetime.strptime(ridetime, '%m/%d/%Y %H:%M')
    else:
        ridetime = datum['Start date']
        date = datetime.strptime(ridetime, '%m/%d/%Y %H:%M')
    
    month = int(date.strftime('%m'))
    hour = int(date.strftime('%H'))
    day_of_week = date.strftime('%A')
    
    return (month, hour, day_of_week)


# Some tests to check that your code works. There should be no output if all of
# the assertions pass. The `example_trips` dictionary was obtained from when
# you printed the first trip from each of the original data files.
tests = {'NYC': (1, 0, 'Friday'),
         'Chicago': (3, 23, 'Thursday'),
         'Washington': (3, 22, 'Thursday')}

for city in tests:
    assert time_of_trip(example_trips[city], city) == tests[city]
    
def type_of_user(datum, city):
    """
    Takes as input a dictionary containing info about a single trip (datum) and
    its origin city (city) and returns the type of system user that made the
    trip.
    
    Remember that Washington has different category names compared to Chicago
    and NYC. 
    """
    
    if city == "Washington":
        if datum["Member Type"] == "Registered":
            user_type = "Subscriber"
        elif datum["Member Type"] == "Casual":
            user_type = "Customer"
    else:
        user_type = datum["usertype"]
    
    return user_type


# Some tests to check that your code works. There should be no output if all of
# the assertions pass. The `example_trips` dictionary was obtained from when
# you printed the first trip from each of the original data files.
tests = {'NYC': 'Customer',
         'Chicago': 'Subscriber',
         'Washington': 'Subscriber'}

for city in tests:
    assert type_of_user(example_trips[city], city) == tests[city]

def condense_data(in_file, out_file, city):
    """
    This function takes full data from the specified input file
    and writes the condensed data to a specified output file. The city
    argument determines how the input file will be parsed.
    
    HINT: See the cell below to see how the arguments are structured!
    """
    
    with open(out_file, 'w') as f_out, open(in_file, 'r') as f_in:
        # set up csv DictWriter object - writer requires column names for the
        # first row as the "fieldnames" argument
        out_colnames = ['duration', 'month', 'hour', 'day_of_week', 'user_type']        
        trip_writer = csv.DictWriter(f_out, fieldnames = out_colnames)
        trip_writer.writeheader()
        
        ## TODO: set up csv DictReader object ##
        trip_reader = csv.DictReader(f_in)

        # collect data from and process each row
        for row in trip_reader:
            # set up a dictionary to hold the values for the cleaned and trimmed
            # data point
            new_point = {}

            ## TODO: use the helper functions to get the cleaned data from  ##
            ## the original data dictionaries.                              ##
            ## Note that the keys for the new_point dictionary should match ##
            ## the column names set in the DictWriter object above.         ##
            new_point['duration'] = duration_in_mins(row, city)
            new_point['month'] = time_of_trip(row, city)[0]
            new_point['hour'] = time_of_trip(row, city)[1]
            new_point['day_of_week'] = time_of_trip(row, city)[2]
            new_point['user_type'] = type_of_user(row, city)

            ## TODO: write the processed information to the output file.     ##
            ## see https://docs.python.org/3/library/csv.html#writer-objects ##
            trip_writer.writerow(new_point)

# Run this cell to check your work
city_info = {'Washington': {'in_file': './data/Washington-CapitalBikeshare-2016.csv',
                            'out_file': './data/Washington-2016-Summary.csv'},
             'Chicago': {'in_file': './data/Chicago-Divvy-2016.csv',
                         'out_file': './data/Chicago-2016-Summary.csv'},
             'NYC': {'in_file': './data/NYC-CitiBike-2016.csv',
                     'out_file': './data/NYC-2016-Summary.csv'}}

for city, filenames in city_info.items():
    condense_data(filenames['in_file'], filenames['out_file'], city)
    print_first_point(filenames['out_file'])

def number_of_trips(filename):
    """
    This function reads in a file with trip data and reports the number of
    trips made by subscribers, customers, and total overall.
    """
    with open(filename, 'r') as f_in:
        # set up csv reader object
        reader = csv.DictReader(f_in)
        
        # initialize count variables
        n_subscribers = 0
        n_customers = 0
        
        # tally up ride types
        for row in reader:
            if row['user_type'] == 'Subscriber':
                n_subscribers += 1
            else:
                n_customers += 1
        
        # compute total number of rides
        n_total = n_subscribers + n_customers
        
        # return tallies as a tuple
        return(n_subscribers, n_customers, n_total)
        
def trip_statistics(data_files):
    '''
    This function reads in files with trip data and reports the highest
    number of trips in a city, highest proportion of trips made by subscribers
    in a city, and highest proportion of trips made by short-term customers in a city.
    '''
    highest_trips = 0   # Stores highest number of trips
    highest_subscribers_proportion = 0  # Stores highest subscribers proportion
    highest_customers_proportion = 0    # Stores highest short-term customers proportion
    
    for city, filename in data_files.items():
        # Fetch city wise trip numbers
        trip_numbers = number_of_trips(filename)
        subscribers_total = trip_numbers[0]
        customers_total = trip_numbers[1]
        trips_total = trip_numbers[2]
        
        # Calculate proportion
        subscribers_proportion = subscribers_total/trips_total
        customers_proportion = customers_total/trips_total
        
        # Find highest number of trips and proportions
        if trips_total > highest_trips:
            highest_trips = trips_total
            highest_trips_city = city
            
        if subscribers_proportion > highest_subscribers_proportion:
            highest_subscribers_proportion = subscribers_proportion
            highest_subscribers_proportion_city = city
            
        if customers_proportion > highest_customers_proportion:
            highest_customers_proportion = customers_proportion
            highest_customers_proportion_city = city
            
    return(highest_trips_city, 
           highest_subscribers_proportion_city, 
           highest_customers_proportion_city)

## Modify this and the previous cell to answer Question 4a. Remember to run ##
## the function on the cleaned data files you created from Question 3.      ##

# data_file = './examples/BayArea-Y3-Summary.csv'
# print(number_of_trips(data_file))

data_files = {'NYC' : './data/NYC-2016-Summary.csv',
              'Chicago' : './data/Chicago-2016-Summary.csv',
              'Washington' : './data/Washington-2016-Summary.csv'}
trip_statistics(data_files)

## Use this and additional cells to answer Question 4b.                 ##
##                                                                      ##
## HINT: The csv module reads in all of the data as strings, including  ##
## numeric values. You will need a function to convert the strings      ##
## into an appropriate numeric type before you aggregate data.          ##
## TIP: For the Bay Area example, the average trip length is 14 minutes ##
## and 3.5% of trips are longer than 30 minutes.                        ##
def get_average_trip_length(filename, city):
    '''
    This function returns average trip time and proportion of trips having
    longer than 30 minutes of trip time.
    '''
    total_trips = 0
    total_trips_time = 0
    total_trips_longer_than_30 = 0
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            total_trips += 1
            total_trips_time += float(row['duration'])
            if float(row['duration']) > 30:
                total_trips_longer_than_30 += 1
    
    average_trip_time = total_trips_time/total_trips
    proportaion_trips_longer_than_30 = total_trips_longer_than_30/total_trips
    
    return(city, average_trip_time, proportaion_trips_longer_than_30)

for city, filename in data_files.items():
    print(get_average_trip_length(filename, city))

## Use this and additional cells to answer Question 4c. If you have    ##
## not done so yet, consider revising some of your previous code to    ##
## make use of functions for reusability.                              ##
##                                                                     ##
## TIP: For the Bay Area example data, you should find the average     ##
## Subscriber trip duration to be 9.5 minutes and the average Customer ##
## trip duration to be 54.6 minutes. Do the other cities have this     ##
## level of difference?                                                ##
def longer_rides_on_average(filename, city):
    '''
    This function returns which kind of riders take longer rides on average.
    '''
    total_customers = 0
    total_customers_trip_time = 0
    total_subscribers = 0
    total_subscribers_trip_time= 0
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            if row['user_type'] == 'Subscriber':
                total_subscribers += 1
                total_subscribers_trip_time += float(row['duration'])
            else:
                total_customers += 1
                total_customers_trip_time += float(row['duration'])
                
    subscribers_average_trip_time = total_subscribers_trip_time/total_subscribers
    customers_average_trip_time = total_customers_trip_time/total_customers
    
    return(city, subscribers_average_trip_time, customers_average_trip_time)
    
print(longer_rides_on_average('./data/Chicago-2016-Summary.csv', 'Chicago'))

# load library
import matplotlib.pyplot as plt

# this is a 'magic word' that allows for plots to be displayed
# inline with the notebook. If you want to know more, see:
# http://ipython.readthedocs.io/en/stable/interactive/magics.html
%matplotlib inline 

# example histogram, data taken from bay area sample
data = [ 7.65,  8.92,  7.42,  5.50, 16.17,  4.20,  8.98,  9.62, 11.48, 14.33,
        19.02, 21.53,  3.90,  7.97,  2.62,  2.67,  3.08, 14.40, 12.90,  7.83,
        25.12,  8.30,  4.93, 12.43, 10.60,  6.17, 10.88,  4.78, 15.15,  3.53,
         9.43, 13.32, 11.72,  9.85,  5.22, 15.10,  3.95,  3.17,  8.78,  1.88,
         4.55, 12.68, 12.38,  9.78,  7.63,  6.45, 17.38, 11.90, 11.52,  8.63,]
plt.hist(data)
plt.title('Distribution of Trip Durations')
plt.xlabel('Duration (m)')
plt.show()

## Use this and additional cells to collect all of the trip times as a list ##
## and then use pyplot functions to generate a histogram of trip times.     ##
def trip_times_plot(filename, city):
    '''
    This functions plots histogram of trip times.
    '''
    trip_times = []
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            trip_times.append(float(row['duration']))
    
    plt.hist(trip_times)
    plt.title('Distribution of trip durations ({})'.format(city))
    plt.xlabel('Duration (m)')
    plt.show()
    
trip_times_plot('./data/Chicago-2016-Summary.csv', 'Chicago')

def trip_times_plot_by_user_types(filename, city):
    '''
    This function plots histogram of trip times by user types.
    '''
    subscriber_trip_times = []
    customer_trip_times = []
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            if row['user_type'] == "Subscriber":
                subscriber_trip_times.append(float(row['duration']))
            else:
                customer_trip_times.append(float(row['duration']))
                
    plt.hist(subscriber_trip_times, 5, (0, 75))
    plt.title('Distribution of subscribers\' trip durations ({})'.format(city))
    plt.xlabel('Duration (m)')
    plt.show()
    
    plt.hist(customer_trip_times, 5, (0, 75))
    plt.title('Distribution of customers\' trip durations ({})'.format(city))
    plt.xlabel('Duration (m)')
    plt.show()

trip_times_plot_by_user_types('./data/Chicago-2016-Summary.csv', 'Chicago')

# Load library
import numpy as np

def monthly_riders_distribution(filename, city):
    '''
    This function displays monthly riders distribution for Subscribers and
    Customers.
    '''
    monthly_subscribers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    monthly_customers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept',
              'Oct', 'Nov', 'Dec']
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            if row['user_type'] == 'Subscriber':
                monthly_subscribers[int(row['month'])-1] += 1
            else:
                monthly_customers[int(row['month'])-1] += 1
    
    arranged_subscribers_data = np.arange(len(monthly_subscribers))
    plt.bar(arranged_subscribers_data, monthly_subscribers, 0.75)
    plt.xticks(arranged_subscribers_data, months)
    plt.xlabel('Months')
    plt.ylabel('Rides')
    plt.title('Month wise distribution of subscribers ({})'.format(city))
    plt.show()
    
    arranged_customers_data = np.arange(len(monthly_customers))
    plt.bar(arranged_customers_data, monthly_customers, 0.75)
    plt.xticks(arranged_customers_data, months)
    plt.xlabel('Months')
    plt.ylabel('Rides')
    plt.title('Month wise distribution of customers ({})'.format(city))
    plt.show()
    
for city, filename in data_files.items():
    monthly_riders_distribution(filename, city)