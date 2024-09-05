# Return the indeces of the two numbers whose sum is the target. They have to be different indeces.
def solution(nums, target):
    size = len(nums)
    for idx1 in range(size):
        for idx2 in range(idx1+1,size):
            if ((nums[idx1]+nums[idx2])==target):
                return [idx1,idx2]

nums = [2,7,11,15]
target = 9
print(solution(nums, target))

nums = [3,2,4]
target = 6
print(solution(nums, target))

nums = [3,3]
target = 6
print(solution(nums, target))