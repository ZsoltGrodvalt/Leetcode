# Method 1: just do it, but not using the fact that they are sorted already
def findMedianSortedArrays(nums1, nums2):
    nums_raw = nums1 + nums2
    nums = sorted(nums_raw)
    l = len(nums)
    if l % 2 == 0:
        # even
        return (nums[int(l/2-1)] + nums[int(l/2)]) / 2
    else:
        # odd
        return nums[l//2]

# Test cases:
a=[1,1,1,3]
b=[2,6,8]

print(findMedianSortedArrays(a,b))