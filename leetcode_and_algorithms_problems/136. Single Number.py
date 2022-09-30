nums = [1, 0, 1]
# nums = [4, 1, 2, 1, 2]
#      [1,1,2,2,4]
res = 0

dict1 = {}

for num in nums:
    dict1[num] = dict1.get(num, 0) + 1

for key, val in dict1.items():
    if val == 1:
        res = key
        break

print(res)
