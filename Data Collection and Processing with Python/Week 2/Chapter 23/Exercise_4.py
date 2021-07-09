# Now define lengths using a list comprehension instead

def lengths(strings):
    length = [len(word) for word in strings]
    return length


lst = ['word', 'car', 'apple', 'shoes']
length = lengths(lst)
print(length)
