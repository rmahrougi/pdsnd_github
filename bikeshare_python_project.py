import time
import pandas as pd
import datetime
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    
    """
    This function gets the user input for a city, month, and day to analyze.
        It returns the city,day,and month to be called in other functions  
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city= input ('which city would you like to see data for chicago, New York, or Washington?\n').lower().strip()
    while (True):
        if (city == 'chicago' or city == 'new york' or city == 'washington' or city =='all'):
            break
        else:
            city = input('Enter Correct city: ').lower().strip()
           

       
    # Gets user input for month (all, january, february, ... , june)
    month = input('\n Which month ? January, February, March, April, May, or June?\n').lower().strip()
    while(True):
        if(month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june' or month == 'all'):
            break
        else:
            month = input('Enter valid month\n').lower().strip()
       
   
    # Get user input for day of week (all, monday, tuesday, ... sunday)
    day =  input('\n Which day you want to see ? monday, tuesday, wednesday, thursday, friday, saturday , sunday or all to display data of all days \n').lower().strip()
    while(True):
   
        if(day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday' or day == 'all'):
            break
        else:
            day = input('Enter valid day\\n').lower().strip()
     
    return city,day,month
   


def load_data(city,month,day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Reading data from the csv files
    df = pd.read_csv(CITY_DATA[city])
    print(df.shape)
     # to_datetime is used to convert date into date format
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
     # extract month, day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day'] = df['Start Time'].dt.day_name()
    print(df['month'].head())
    print(month + day)
    #filter data by day
    if month != 'all':  
        #filter by month
        df = df[df['month'] == month.title()]
    print(df.shape)
   #filter data by day
    if day != 'all':
       df = df[df['day'] == day.title()]
    
    print(df.shape)
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
               
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
   
    # display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month is ' + str(common_month))
   
    # display the most common day of week
    common_day = df['day'].mode() [0]
    print('Most common day is ' + str(common_day))
   
     # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode() [0]
    print('Most popular hour is ' + str(common_hour))
               
 
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()
    print('Most common start station is {}'.format(common_start_station))

    # displays most commonly used end station
    common_end_station = df['End Station'].mode()
    print('Most common end station is {}'.format(common_end_station))

    # displays most frequent combination of start station and end station trip
    combination_station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', combination_station)
   

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # displays total travel time

    totalTripDuration = df['Trip Duration'].sum()
    print('Total Travel Time is',totalTripDuration)

    #  displays mean travel time
               
    AvgTripDuration = df['Trip Duration'].mean()
    print('Average Travel Time is',AvgTripDuration)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Displays counts of user types
    totalsubscribers = df['User Type'].str.count('Subscriber').sum()
    totalcustomers = df['User Type'].str.count('Customer').sum()
    print('\n Number of subscribers are {}\n'.format(int(totalsubscribers)))
    print('\n Number of customers are {}\n'.format(int(totalcustomers)))

   # Displays counts of gender only for chicago and nyc
    if('Gender' in df):
        male_count = df['Gender'].str.count('Male').sum()
        female_count = df['Gender'].str.count('Female').sum()
        print('\nNumber of male users are {}\n'.format(int(male_count)))
        print('\nNumber of female users are {}\n'.format(int(female_count)))


    # Displays earliest, most recent, and most common year of birth only for nyc and chicago
    if('Birth Year' in df):
        earliest_birth_year = df['Birth Year'].min()
        oldest_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()
        print('The oldest Birth Year is {}\n The Earliest Birth Year is {}\n ,and The Most popular Birth Year is {}\n'.format(int(earliest_birth_year), int(oldest_birth_year), most_common_birth_year))



def main():
    while True:
        city, day , month = get_filters()
        df = load_data(city, month, day)
        #get the raw data 
        get_raw_data =input(" Would you like to see the raw data? ").strip().lower()
        start = 0
        end = 5
        while(get_raw_data == 'yes'):
            print(df.iloc[start:end])
            start += 5 
            end += 5
            get_raw_data = input (" would you like to see more data? ").strip().lower()

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\n Would you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print(" I'm not sure if you want to start over.. please type yes or No")
            break


if __name__ == "__main__":
    main()