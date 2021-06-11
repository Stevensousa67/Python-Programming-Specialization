# Provided is a list of numbers. For each of the numbers in the list, determine whether they are odd. If the number is
# odd, add True to a new list called is_odd. If the number is even, then add False.

lst = list(range(1, 10))
print(lst)
is_odd = []

for x in lst:
    if x % 2 != 0:
        is_odd.append(True)
    else:
        is_odd.append(False)

print(is_odd)
