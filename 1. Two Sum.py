# Return the indeces of the two numbers whose sum is the target. They have to be different indeces.

# Comparing all the numbers...
def solution1(nums, target):
    size = len(nums)
    for idx1 in range(size):
        diff = target - nums[idx1]
        for idx2 in range(idx1+1,size):
            if (nums[idx2]==diff):
                return [idx1,idx2]

# Using a dictionary and only iterating through the list once
def solution2(nums, target):
    dict = {}
    for idx, num in enumerate(nums):
        difference = target - num
        if difference in dict:
            return [idx, dict[difference]]
        else:
            dict[num] = idx

nums = [2,7,11,15]
target = 9
print(solution1(nums, target))

nums = [3,2,4]
target = 6
print(solution1(nums, target))

nums = [3,3]
target = 6
print(solution1(nums, target))