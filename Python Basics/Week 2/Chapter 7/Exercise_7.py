# Assume you have a list of numbers 12, 10, 32, 3, 66, 17, 42, 99, 20
# Write a loop that prints each of the numbers on a new line.
# Write a loop that prints each number and its square on a new line.

lst = [12, 10, 32, 3, 66, 17, 42, 99, 20]

for number in lst:
    print('Current number:', number)

for num in lst:
    print('Current number:', num, 'and its square is:', num * num)
