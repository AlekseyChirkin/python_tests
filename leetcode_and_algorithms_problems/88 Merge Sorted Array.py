# nums1 = [-4, 0, 0, 1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0]
# m = 6
# nums2 = [2, 5, 6, 10, 99, 103, 200, 1000]
# n = 8

nums1 = [2, 0]
m = 1
nums2 = [1]
n = 1

while n > 0:
    if nums1[m - 1] <= nums2[n - 1] or m <= 0:
        nums1[m + n - 1] = nums2[n - 1]
        n -= 1
    else:
        nums1[m + n - 1] = nums1[m - 1]
        m -= 1

print(nums1)
