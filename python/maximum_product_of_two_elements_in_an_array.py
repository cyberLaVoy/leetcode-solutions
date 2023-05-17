import math

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        """
        Finds the maximum product of any two non-overlapping integers in the given list.
        Args:
            nums: A list of integers.
        Returns:
            The maximum product of any two non-overlapping integers in the given list.
        Raises:
            TypeError: If the input `nums` is not a list or contains non-integer values.
        """
        # Set the initial maximum product to negative infinity
        max_product = -math.inf
        # Loop through each pair of integers in the list
        for i in range(len(nums)):
            for j in range(len(nums)):
                # Skip if the indices are the same (i.e., the same number is used twice)
                if i != j:  
                    # Calculate the product of the two integers minus 1
                    product = (nums[i]-1)*(nums[j]-1)
                    # Update the maximum product if the calculated product is greater
                    if product > max_product:
                        max_product = product
        return max_product