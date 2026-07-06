#reduce
nums = [1, 2, 3, 4, 5]
from functools import reduce
total = reduce(lambda a, b: a + b, nums)
print(total)  # Output: 15