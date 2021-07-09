# Define longwords using a list comprehension

def longwords_Li_Comp(lst):
    longwords_lst = [word for word in lst if len(word) > 4]
    return longwords_lst


lst = ['play', 'gym', 'useful', 'steven', 'software']
lst2 = longwords_Li_Comp(lst)
print(lst2)
