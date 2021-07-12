# Use manual accumulation to define the lengths function below.

def lengths(strings):
    """lengths takes a list of strings as input and returns a list of numbers that are the lengths
    of strings in the input list. Use manual accumulation!"""
    # fill in this function's definition to make the test pass.
    length = []
    for word in strings:
        length.append(len(word))
    return length


lst = ['word', 'car', 'apple', 'shoes']
length = lengths(lst)
print(length)
