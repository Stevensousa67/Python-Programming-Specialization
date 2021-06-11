# Provided are the lengths of two sides of a right-angled triangle. Assign the length of the hypotenuse the the variable
# hypo_len. (Hint: x ** 0.5 will return the square root, or use sqrt from the math module)

import math

side_1 = 4
side_2 = 3
hypo_len = math.sqrt(side_1*side_1 + side_2*side_2)

print(hypo_len)
