# Challenge: Below, we have provided a list of lists that contain numbers. Using list comprehension, create a new list
# threes that contains all the numbers from the original list that are divisible by 3.
# This can be accomplished in one line of code.

nums = [[4, 3, 12, 10], [8, 7, 6], [5, 18, 15, 7, 11], [9, 4], [24, 20, 17], [3, 5]]
threes = []
[threes.append(x) for x in nums for x in x if x % 3 == 0]
print(threes)
