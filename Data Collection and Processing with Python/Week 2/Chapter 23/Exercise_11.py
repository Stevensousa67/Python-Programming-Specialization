# Write a function called longlengths that returns the lengths of those strings that have at least 4 characters. Try it
# with a list comprehension.

def longlengths(strings):
    longwords = [len(word) for word in strings if len(word) >= 4]
    return longwords


lst = ['play', 'gym', 'useful', 'steven', 'software']
lst2 = longlengths(lst)
print(lst2)
