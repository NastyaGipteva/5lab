from random import randint
m = int(input())
n = int(input())
nums1 = [randint(0, m) for i in range(m)]
nums2 = [randint(0, n) for h in range(n)]
def medians(nums1, nums2):
    nums_new = nums1 + nums2
    sr = sum(nums_new)/len(nums_new)
    return sr
print(medians(nums1, nums2))
