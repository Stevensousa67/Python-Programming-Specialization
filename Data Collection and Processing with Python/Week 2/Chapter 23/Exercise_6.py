# Write a function called positives_Fil that receives list of things as the input and returns a list of only the
# positive things, [3, 5, 7], using the filter function.

def positives_Fil(lst):
    pos_lst = list(filter(lambda num: num > 0, lst))
    return pos_lst


things = [3, 5, -4, 7]
pos_lst = positives_Fil(things)
print(pos_lst)
