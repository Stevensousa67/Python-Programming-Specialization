# Provided is a list of numbers. For each of the numbers in the list, determine whether they are even. If the number is
# even, add True to a new list called is_even. If the number is odd, then add False.

lst = list(range(1, 10))
print(lst)
is_even = []

for x in lst:
    if x % 2 == 0:
        is_even.append(True)
    else:
        is_even.append(False)

print(is_even)
