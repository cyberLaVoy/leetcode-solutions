class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        num_unique_candies = len(set(candyType))
        num_advised_candies = len(candyType) // 2
        max_num_consumable_candies = min(num_unique_candies, num_advised_candies)
        return max_num_consumable_candies