# Define longwords using manual accumulation

def longwords(lst):
    longwords_lst = []
    for word in lst:
        if len(word) > 4:
            longwords_lst.append(word)
    return longwords_lst


lst = ['play', 'gym', 'useful', 'steven', 'software']
lst2 = longwords(lst)
print(lst2)
