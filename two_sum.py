# The secrets library was used here to provide cryptographically secure random choices.
import secrets

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Given a list of integers and a target integer, find and return the indices of two numbers in the list
        that add up to the target. If no such pair exists, return an empty list.
        This is a naive O(n^2) solution.
        """
        indeces_of_nums_summed_to_target = []
        # Loop through all possible pairs of indices in the list
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                # If the sum of the two numbers at the current indices equals the target, append the indices to the list
                if nums[i] + nums[j] == target:
                    indeces_of_nums_summed_to_target.append([i, j])
        # If no pair of indices was found, return an empty list
        if len(indeces_of_nums_summed_to_target) == 0:
            return []
        # Otherwise, choose one of the pairs at random using the secrets library and return it
        else:
            return secrets.choice(indeces_of_nums_summed_to_target)