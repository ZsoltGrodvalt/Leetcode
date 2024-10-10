class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        def iLessThanInRight(i, num_i, Right):
            for key,value in Right.items():
                if (num_i <= value) & (i < key):
                    return True, key - i
            return False, 0
        
        def jGreaterThanInLeft(j, num_j, Left):
            for key,value in Left.items():
                if (num_j >= value) & (j > key):
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
            if less & (width > maxwidth):
                maxwidth = width
                print(f'maxwidth >>> {maxwidth}')
            print(f'update Left with {i} : {nums[i]}')
            less_self, width = jGreaterThanInLeft(i,nums[i], Left)
            if less_self & (width > maxwidth):
                maxwidth = width
                print(f'maxwidth >>> {maxwidth}')
            Left[i] = nums[i]

            print(f'check {Left} <= {nums[j]}')
            # check all the numbers in Left if they are smaller then nums[i]
            greater, width = jGreaterThanInLeft(j,nums[j], Left)
            if greater & (width > maxwidth):
                maxwidth = width
                print(f'maxwidth >>> {maxwidth}')
            greater_self, width = iLessThanInRight(j,nums[j], Right)
            if greater_self & (width > maxwidth):
                maxwidth = width
                print(f'maxwidth >>> {maxwidth}')

            print(f'update Right with {j} : {nums[j]}')
            Right[j] = nums[j]

            i += 1
            j -= 1

        
        print(f'check {nums[i]} <= {Right}')
        # check all the numbers in Right if they are smaller then nums[i]
        less, width = iLessThanInRight(i,nums[i], Right)
        if less & (width > maxwidth):
            maxwidth = width
            print(f'maxwidth >>> {maxwidth}')
        print(f'update Left with {i} : {nums[i]}')
        less_self, width = jGreaterThanInLeft(i,nums[i], Left)
        if less_self & (width > maxwidth):
            maxwidth = width
            print(f'maxwidth >>> {maxwidth}')

        Left[i] = nums[i]

        print(f'check {Left} <= {nums[j]}')
        # check all the numbers in Left if they are smaller then nums[i]
        greater, width = jGreaterThanInLeft(j,nums[j], Left)
        if greater & (width > maxwidth):
            maxwidth = width
            print(f'maxwidth >>> {maxwidth}')
        greater_self, width = iLessThanInRight(j,nums[j], Right)
        if greater_self & (width > maxwidth):
            maxwidth = width
            print(f'maxwidth >>> {maxwidth}')

        print(f'update Right with {j} : {nums[j]}')
        Right[j] = nums[j]
        
        return maxwidth

        
# if __name__ == '__main__':


#     nums1 = [98,98,98,98,95,95,92,90,90,89,89,89,89,87,86,85,85,85,84,83,81,80,79,78,78,76,76,75,75,74,74,73,73,73,72,71,71,71,69,68,68,68,66,66,62,60,58,57,57,56,56,56,55,55,54,54,52,52,51,50,50,49,49,48,47,46,46,44,43,43,42,40,39,38,38,38,35,35,35,34,34,34,29,26,23,19,17,15,15,13,11,7,6,6,4,4,3,2,2,1]
#     nums2 = [9,8,1,0,1,9,4,0,4,1]

#     print(Solution.maxWidthRamp(nums1))