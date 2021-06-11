# Write code that asks the user to enter a numeric score (0-100). In response, it should print out the score and
# corresponding letter grade, according to the table below.

grade = int(input('Enter a grade from 0 - 100: '))
if grade > 100 or grade < 0:
    print("Invalid grade.")
    exit(0)
else:
    if grade < 60:
        print(grade, '= F')
    elif grade < 70:
        print(grade, '= D')
    elif grade < 80:
        print(grade, '= C')
    elif grade < 90:
        print(grade, '= B')
    else:
        print(grade, '= A')
