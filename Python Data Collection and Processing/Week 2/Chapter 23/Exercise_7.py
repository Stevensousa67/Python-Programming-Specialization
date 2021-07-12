# Write a function called positives_Li_Com that receives list of things as the input and returns a list of only the
# positive things, [3, 5, 7], using the list comprehension.

def positives_Li_Com(lst):
    pos_lst = [num for num in lst if num > 0]
    return pos_lst


things = [3, 5, -4, 7]
pos_lst = positives_Li_Com(things)
print(pos_lst)
