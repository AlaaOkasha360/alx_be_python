from datetime import datetime, timedelta, time

def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:",current_date.strftime('%Y-%m-%d %H:%M:%S'))
    return current_date

def calculate_future_date(number_of_days, current_date):
    added_days = timedelta(days=number_of_days)
    future_date = current_date+added_days
    print("Future date:",future_date.strftime('%Y-%m-%d %H:%M:%S'))

curr = display_current_datetime()
add = int(input("Enter the number of days to add to the current date: "))
calculate_future_date(add, curr)

