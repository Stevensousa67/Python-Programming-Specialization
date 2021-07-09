# Write a function called longlengths that returns the lengths of those strings that have at least 4 characters.
# Try it using map and filter.

def longlengths(strings):
    new_lst = map(lambda x: len(x), strings)
    new_lst1 = filter(lambda x: x >= 4, new_lst)
    return list(new_lst1)


lst = ['play', 'gym', 'useful', 'steven', 'software']
lst2 = longlengths(lst)
print(lst2)
