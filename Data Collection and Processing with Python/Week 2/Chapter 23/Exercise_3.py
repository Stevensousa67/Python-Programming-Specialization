# Now define lengths using map instead

def lengths(strings):
    length = list(map(lambda word: len(word), strings))
    return length


lst = ['word', 'car', 'apple', 'shoes']
length = lengths(lst)
print(length)
