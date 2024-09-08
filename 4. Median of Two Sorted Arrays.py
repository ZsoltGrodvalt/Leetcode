# Method 1: just do it, but not using the fact that they are sorted already
# def findMedianSortedArrays(nums1, nums2):
#     nums_raw = nums1 + nums2
#     nums = sorted(nums_raw)
#     l = len(nums)
#     if l % 2 == 0:
#         # even
#         return (nums[int(l/2-1)] + nums[int(l/2)]) / 2
#     else:
#         # odd
#         return nums[l//2]

# Method 2: only sort the two arrays until we reach the median
def findMedianSortedArrays(nums1, nums2):
    len_tot = len(nums1) + len(nums2)
    i1=0
    i2=0
    l1 = len(nums1)
    l2 = len(nums2)
    # l1 is always the longer
    if l1 < l2:
        nums1, nums2 = nums2, nums1
        l1,l2=l2,l1

    nums = []
    if len_tot % 2 == 0:
        print('even')
        target = len_tot/2
        print(f'target:{target}')
        while (i1<l1) & (i2<l2) & (len(nums) != target+1):
            if nums1[i1] < nums2[i2]:
                nums.append(nums1[i1])
                i1 += 1
            else:
                nums.append(nums2[i2])
                i2 += 1
        if (i1<l1) & (len(nums) != target+1):
            while len(nums) != target+1:
                nums.append(nums1[i1])
                i1 += 1
            print(nums)
            return (nums[-1]+nums[-2])/2
        if (i2<l2) & (len(nums) != target+1):
            while len(nums) != target+1:
                nums.append(nums2[i2])
                i2 += 1
            print(nums)
            return (nums[-1]+nums[-2])/2
        print(nums)
        return (nums[-1]+nums[-2])/2
    else:
        print('odd')
        target = len_tot//2
        print(f'target:{target}')
        while (i1<l1) & (i2<l2) & (len(nums) != target+1):
            if nums1[i1] < nums2[i2]:
                nums.append(nums1[i1])
                i1 += 1
            else:
                nums.append(nums2[i2])
                i2 += 1
        if (i1<l1) & (len(nums) != target+1):
            while len(nums) != target+1:
                nums.append(nums1[i1])
                i1 += 1
            print(nums)
            return nums[-1]
        if (i2<l2) & (len(nums) != target+1):
            while len(nums) != target+1:
                nums.append(nums2[i2])
                i2 += 1
            print(nums)
            return nums[-1]
        print(nums)
        return nums[-1]
        
        


# Test cases:
a=[1,3]
b=[2,7]
print(findMedianSortedArrays(a,b))