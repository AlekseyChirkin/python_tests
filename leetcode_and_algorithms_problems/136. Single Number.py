nums = [1, 0, 1]

nums = sorted(nums)
#      [0, 1, 1]

for i in range(len(nums)):
    print(nums)
    x1 = nums[i]
    x2 = 0

    l = i
    r = len(nums) - 1
    m = 0

    while l < r:
        m = (l + r) // 2
        if nums[m] > nums[l]:
            l = m + 1
        elif nums[m] < nums[r]:
            r = m
        else:
            x2 = nums[m]
            break

    if x1 == x2:
        continue
    else:
        print(x1)
