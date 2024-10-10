class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        def iLessThanInRight(i, num_i, Right):
            for key,value in Right.items():
                if (num_i <= value) & (i != key):
                    return True, key - i
            return False, 0
        
        def jGreaterThanInLeft(j, num_j, Left):
            for key,value in Left.items():
                if (num_j >= value) & (j != key):
                    return True, j - key
            return False, 0

        print(nums)
        Left = {}
        Right = {}

        maxwidth = 0
        i = 0
        j = len(nums)-1

        Left[i] = nums[i]
        Right[j] = nums[j]

        # initial tests
        if len(nums) == 0:
            return 0

        # main algorithm
        while i < j:
            print(f'check {nums[i]} <= {Right}')
            # check all the numbers in Right if they are smaller then nums[i]
            less, width = iLessThanInRight(i,nums[i], Right)
            if less:
                print('True, return')
                return width
            print(f'update Left with {i} : {nums[i]}')
            less_self, width = jGreaterThanInLeft(i,nums[i], Left)
            if less_self & (width > maxwidth):
                maxwidth = width
            Left[i] = nums[i]

            print(f'check {Left} <= {nums[j]}')
            # check all the numbers in Left if they are smaller then nums[i]
            greater, width = jGreaterThanInLeft(j,nums[j], Left)
            if greater:
                print('True, return')
                return width
            greater_self, width = iLessThanInRight(j,nums[j], Right)
            if greater_self & (width > maxwidth):
                maxwidth = width
            print(f'update Right with {j} : {nums[j]}')
            Right[j] = nums[j]

            i += 1
            j -= 1

        
        print(f'check {nums[i]} <= {Right}')
        # check all the numbers in Right if they are smaller then nums[i]
        less, width = iLessThanInRight(i,nums[i], Right)
        if less:
            print('True, return')
            return width
        print(f'update Left with {i} : {nums[i]}')
        less_self, width = jGreaterThanInLeft(i,nums[i], Left)
        if less_self & (width > maxwidth):
            maxwidth = width
        Left[i] = nums[i]

        print(f'check {Left} <= {nums[j]}')
        # check all the numbers in Left if they are smaller then nums[i]
        greater, width = jGreaterThanInLeft(j,nums[j], Left)
        if greater:
            print('True, return')
            return width
        greater_self, width = iLessThanInRight(j,nums[j], Right)
        if greater_self & (width > maxwidth):
            maxwidth = width
        print(f'update Right with {j} : {nums[j]}')
        Right[j] = nums[j]
        
        return maxwidth

        
# if __name__ == '__main__':


#     nums1 = [6,0,8,2,1,5]
#     nums2 = [9,8,1,0,1,9,4,0,4,1]

#     print(Solution.maxWidthRamp(nums1))
#     print(Solution.maxWidthRamp(nums2))