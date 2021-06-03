# Challenge: The formula for computing the final amount if one is earning compound interest
# Write a Python program that assigns the principal amount of 10000 to variable P, assign to n the value 12, and
# assign to r the interest rate of 8% (0.08). Then have the program prompt the user for the number of years, t,
# that the money will be compounded for. Calculate and print the final amount after t years.

p = 10000
r = .08
n = 12
t = int(input("Enter amount of time in years: "))
power = n*t

A = p * (1 + (r/n))**power
A = round(A, 2)

print("Final amount: ", A)
