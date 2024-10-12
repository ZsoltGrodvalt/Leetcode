def maxWidthRamp(nums):
    # preprocessing
    width = 0
    l = 0
    max_right = [0]*len(nums)
    i = len(nums)-1
    prev_max = 0
    for num in reversed(nums):
        max_right[i] = max(prev_max, nums[i])
        prev_max = max_right[i]
        i -= 1
    
    # going through with two pointers
    # (sliding window)
    for r in range(len(nums)):
        while nums[l] > max_right[r]:
            l += 1
        width = max(width, r-l)

    return width
        
if __name__ == '__main__':
    #                  [8,8,8,5,5,5]  
    print(maxWidthRamp([6,0,8,2,1,5]))