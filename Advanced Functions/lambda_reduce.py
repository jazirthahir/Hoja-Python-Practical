#reduce
nums = [1, 2, 3, 4, 5]
from functools import reduce #this is a function from a standard library that allows us to reduce a list to a single value by applying a function cumulatively to the items of the list.
total = reduce(lambda a, b: a + b, nums)
print(total)  # Output: 15