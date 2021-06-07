# Write a program that will compute MPG for a car. Prompt the user to enter the number of miles driven and the number of
# gallons used. Print a nice message with the answer.

miles_driven = int(input("Enter amount of miles driven: "))
gallons_used = int(input("Enter amount of gallons used: "))
mpg = miles_driven/gallons_used

print(mpg)