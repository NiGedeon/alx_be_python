import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: ", formatted)
    return current_date

current_date = display_current_datetime()

ndays = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date(current_date, ndays): 
    
    future_date = current_date + datetime.timedelta(days=ndays)
    formated = future_date.strftime("%Y-%m-%d")
    print("Future date: ",formated)
calculate_future_date(current_date,ndays)
