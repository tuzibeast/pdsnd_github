import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }




def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data for Chicago, New York City or Washington?: ').lower()
        if city.lower() in (CITY_DATA):
            print('\nSelected city: {}\n'.format(city))
            break
        else:
            print('\nNot a valid selection. Please try again: ')
            continue

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        month = input('What month would you like to filter by? Enter: January, February, March, April, May, June, or All: ').lower()
        if month.lower() in months:
            print('\nSelected month: {}\n'.format(month))
            break
        else:
            print('\nNot a valid selection. Please try again: ')
            continue



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
        day = input('What day of the week would you like to filter by?\nEnter: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or All: ').lower()
        if day in days:
            print('\nSelected day: {}\n'.format(day))
            break
        else:
            print('\nNot a valid selection. Please try again: ')
            continue

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])


    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]



    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    common_month = df['month'].mode()[0]

    print('The most common month is: ' , common_month)

    # TO DO: display the most common day of week

    common_day = df['day_of_week'].mode()[0]
    print('The most common day of the week is: ', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour to start travel is: ' , common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is: ', most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is: ', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip



    df['common_route'] = 'between: ' + df['Start Station'] + ' and ' + df['End Station']
    #To calculate the most frequent route combination between Start Station and End Station we can also use 'groupby' in pandas
    
    most_common_route = df['common_route'].mode()[0]
    print('The most common route is', most_common_route)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total time of travel is: ', total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Average time of travel is: ', mean_travel_time)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_type = df['User Type'].value_counts()

    print('User count:', user_type)

    # TO DO: Display counts of gender

    if "Gender" in df.columns:
        gender = df['Gender'].value_counts()
        print('Gender count:', gender)

    else:
        print('There is no gender information for this city')

    # TO DO: Display earliest, most recent, and most common year of birth
    # TO DO: Account for missing columns in Washington data

    if "Birth Year" in df.columns:
        earliest_birth_year = min(df['Birth Year'])

        print('The earliest birth year is:', earliest_birth_year)

        recent_birth_year = max(df['Birth Year'])

        print('The most recent birth year is:', recent_birth_year)

        common_birth_year = df['Birth Year'].value_counts().idxmax()

        print('The most common birth year is:', common_birth_year)

    else:
        print('There is no birth information for this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    view = input('Would you like to see more data:   yes or no ?\n').lower()

    n = 0

    while view == 'yes':

        print(df[n:n+5])

        n += 5

        view = input('Would you like to see more data:  yes or no ?\n')

        print("\nThis took %s seconds." % (time.time() - start_time))

        print('-'*40)






def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)


        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
