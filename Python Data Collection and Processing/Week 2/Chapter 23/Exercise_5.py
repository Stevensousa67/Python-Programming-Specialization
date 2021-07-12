# Write a function called positives_Acc that receives list of numbers as the input (like [3, -1, 5, 7]) and returns a
# list of only the positive numbers, [3, 5, 7], via manual accumulation.

def positives_Acc(lst):
    pos_lst = []
    for num in lst:
        if num < 0:
            continue
        else:
            pos_lst.append(num)
    return pos_lst


things = [3, 5, -4, 7]
pos_lst = positives_Acc(things)
print(pos_lst)
