# You’re going to write a function that takes a string as a parameter and returns a list of the five most frequent
# characters in the string.

def find_5_most_freq_chars(s):
    dict = {}
    for char in list(s):
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1
    first_5 = sorted(dict, key=lambda k: dict[k], reverse=True)  # lambda function is sorting by value
    return first_5[:5]


string = "inconstitucionalissimamente"
print(find_5_most_freq_chars(string))
