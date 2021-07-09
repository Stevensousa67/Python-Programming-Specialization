# Define longwords using filter

def longwords_Fil(lst):
    longwords_lst = list(filter(lambda word: len(word) > 4, lst))
    return longwords_lst


lst = ['play', 'gym', 'useful', 'steven', 'software']
lst2 = longwords_Fil(lst)
print(lst2)
