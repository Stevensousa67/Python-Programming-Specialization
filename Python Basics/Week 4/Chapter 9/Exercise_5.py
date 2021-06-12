# The string module provides sequences of various types of Python characters. It has an attribute called digits that
# produces the string ‘0123456789’. Import the module and assign this string to the variable nums. Below, we have
# provided a list of characters called chars. Using nums and chars, produce a list called is_num that consists of
# tuples. The first element of each tuple should be the character from chars, and the second element should be a Boolean
# that reflects whether or not it is a Python digit.

import string

chars = ['h', '1', 'C', 'i', '9', 'True', '3.1', '8', 'F', '4', 'j']
nums = string.digits

is_num = []

for element in chars:
    is_num.append((element, element in nums))

print(is_num)

