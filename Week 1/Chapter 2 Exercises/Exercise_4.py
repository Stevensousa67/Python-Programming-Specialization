# It is possible to name the days 0 thru 6 where day 0 is Sunday and day 6 is Saturday. If you go on a wonderful holiday
# leaving on day number 3 (a Wednesday) and you return home after 10 nights you would return home on a Saturday (day 6).
# Write a general version of the program which asks for the starting day number, and the length of your stay, and it
# will tell you the number of day of the week you will return on.

current_day = int(input("Enter a number from 0 to 6, where 0 is Sunday and 6 is Saturday: "))

if current_day > 6 or current_day < 0:
    print("Invalid day.")
    exit()

trip_days = int(input("Enter how many days your trip will last: "))

for x in range(trip_days):
    current_day += 1
    if current_day > 6:
        current_day = 0

if current_day == 0:
    current_day = "Sunday"
elif current_day == 1:
    current_day = "Monday"
elif current_day == 2:
    current_day = "Tuesday"
elif current_day == 3:
    current_day = "Wednesday"
elif current_day == 4:
    current_day = "Thursday"
elif current_day == 5:
    current_day = "Friday"
elif current_day == 6:
    current_day = "Saturday"

print("It'll be a", current_day, "when you come back!")
