# Challenge: The nested for loop given takes in a list of lists and combines the elements into a single list.
# Do the same thing using a list comprehension for the list L. Assign it to the variable result2.

def onelist(lst):
    result = []
    for each_list in lst:
        for item in each_list:
            result.append(item)
    return result


L = [["hi", "bye"], ["hello", "goodbye"], ["hola", "adios", "bonjour", "au revoir"]]

result2 = [word for lst in L for word in lst]
print(result2)
