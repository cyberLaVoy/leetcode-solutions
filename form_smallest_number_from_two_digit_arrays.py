import math

class Solution:
    def minNumber(self, nums1: list[int], nums2: list[int]) -> int:
        min_number = math.inf
        # Combination check
        for num1 in nums1:
            for num2 in nums2:
                concat_nums_direction_1 = int(str(num1) + str(num2))
                concat_nums_direction_2 = int(str(num2) + str(num1))
                if concat_nums_direction_1 < min_number:
                    min_number = concat_nums_direction_1
                if concat_nums_direction_2 < min_number:
                    min_number = concat_nums_direction_2
        # Single digit check 
        for num1 in nums1:
            if num1 in nums2 and num1 < min_number:
                min_number = num1
        return min_number