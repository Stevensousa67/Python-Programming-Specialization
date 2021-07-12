# Write a function that takes a list of numbers and returns the sum of the squares of all the numbers.
# Try it using an accumulator pattern.

def sumSquares(L):
    sum = 0
    for num in L:
        squared = num * num
        sum += squared
    squared_sum = sum
    return squared_sum


nums = [3, 2, 2, -1, 1]
squared_sum = sumSquares(nums)
print(squared_sum)
