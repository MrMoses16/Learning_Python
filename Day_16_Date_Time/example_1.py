from datetime import datetime

# Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print("Get the current day, month, year, hour, minute and timestamp from datetime module")
print(f"Today's date is {month}/{day}/{year}. The time is {hour}:{minute}. The timestamp is {timestamp}\n")

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
now = datetime.now()
time = now.strftime("%H:%M:%S")
date = now.strftime("%d/%m/%Y")
print("Format the current date using this format: \"%m/%d/%Y, %H:%M:%S\"")
print(f"{date} {time}\n")

# Today is 5 December, 2019. Change this time string to time.
date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("Today is 5 December, 2019. Change this time string to time.")
print(f"{date_string} converts to {date_object}\n")

# Calculate the time difference between now and new year.
time = datetime.now()
today = datetime(year = int(time.strftime("%Y")), month = int(time.strftime("%m")), day = int(time.strftime("%d")), hour = int(time.strftime("%H")), minute = int(time.strftime("%M")), second = int(time.strftime("%S")))
new_year = datetime(year = int(time.strftime("%Y")) + 1, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = new_year - today
print("Calculate the time difference between now and new year.")
print(f"{diff}\n")

# Calculate the time difference between 1 January 1970 and now.
time = datetime.now()
today = datetime(year = int(time.strftime("%Y")), month = int(time.strftime("%m")), day = int(time.strftime("%d")), hour = int(time.strftime("%H")), minute = int(time.strftime("%M")), second = int(time.strftime("%S")))
date = datetime(year = 1970, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = today - date
print("Calculate the time difference between 1 January 1970 and now.")
print(diff)