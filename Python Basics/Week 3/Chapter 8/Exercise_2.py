# A year is a leap year if it is divisible by 4. If the year can be evenly divided by 100, it is NOT a leap year, unless
# the year is also evenly divisible by 400. Then it is a leap year. Write code that asks the user to input a year and
# output True if it’s a leap year, or False otherwise. Use if statements.

def isLeapYear(x):
    """Function that finds if a given year or not"""
    is_leap = False
    if (x % 4) == 0 and (x % 100) != 0:
        is_leap = True
    elif (x % 400) == 0:
        is_leap = True
    return is_leap


year = int(input('Enter a year to discover if it is a leap year: '))
print(isLeapYear(year))
