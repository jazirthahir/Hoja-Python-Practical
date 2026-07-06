list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for i in range(1,len(list),2):
    print(list[i])


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
even_list = []
for num in nums:
    if num % 2 == 0:
        even_list.append(num)
       
print(nums)
print(even_list)
