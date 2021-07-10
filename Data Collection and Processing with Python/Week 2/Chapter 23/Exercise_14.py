# Write a function that takes a list of numbers and returns the sum of the squares of all the numbers.
# Try it using map and sum.

def sumSquares(L):
    sum_squared = sum(list(map(lambda x: x * x, L)))
    return sum_squared


nums = [3, 2, 2, -1, 1]
sum_squared = sumSquares(nums)
print(sum_squared)
