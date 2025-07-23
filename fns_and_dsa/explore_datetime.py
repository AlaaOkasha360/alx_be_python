from datetime import datetime, timedelta, time

def display_current_datetime():
    current_date = datetime.now()
    return current_date

def calculate_future_date(number_of_days, current_date):
    added_days = timedelta(days=number_of_days)
    future_date = current_date+added_days
    print("Future date:",future_date)

print("Current date and time:",display_current_datetime())
add = int(input("Enter the number of days to add to the current date: "))
calculate_future_date(add, display_current_datetime())

