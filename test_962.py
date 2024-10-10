from Maximum_Width_Ramp_962 import Solution   # The code to test
import unittest   # The test framework

class Test_Test962(unittest.TestCase):
    def test_1(self):
        nums1 = [6,0,8,2,1,5]
        self.assertEqual(Solution.maxWidthRamp(nums1), 4)

    def test_2(self):
        nums2 = [9,8,1,0,1,9,4,0,4,1]
        self.assertEqual(Solution.maxWidthRamp(nums2), 7)

    def test_82(self):
        self.assertEqual(Solution.maxWidthRamp([2,2,1]), 1)

    def test_88(self):
        self.assertEqual(Solution.maxWidthRamp([3,4,2,1]), 1)

    def test_87(self):
        self.assertEqual(Solution.maxWidthRamp([1,0]), 0)


if __name__ == '__main__':
    unittest.main()