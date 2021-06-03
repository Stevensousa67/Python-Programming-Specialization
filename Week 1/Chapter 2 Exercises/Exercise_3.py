# Challenge: Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight).
# If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm).
# Write a Python program to solve the general version of the above problem. Ask the user for the time now (in hours),
# and then ask for the number of hours to wait for the alarm. Your program should output what the time will be on the
# clock when the alarm goes off.

current_time = int(input("What time is it now in military time? "))

if current_time > 23 or current_time < 0:   # Check if time is valid
    print("That is an invalid time.")
    exit()

timer = int(input("How many hours to wait? "))

for x in range(timer):
    current_time += 1
    if current_time > 23:
        current_time = 0

if current_time < 12:
    print("After waiting", timer,  "hours, it'll be", current_time, "am")
else:
    print("After waiting", timer, "hours, it'll be", current_time, "pm")
