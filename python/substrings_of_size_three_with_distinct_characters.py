class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        """
        Counts the number of "good" substrings of length 3 in a given string. 
        Where a "good" substring is defined as a substring that contains only distinct characters. 
        Args:
            s (str): The input string.
        Returns:
            int: The count of "good" substrings.
        """
        # List to store all size 3 substrings
        size_three_substrings = []  
        # Generate all size 3 substrings by iterating over the string
        for i in range(len(s)-2):
            size_three_substring = s[i:i+3]
            size_three_substrings.append(size_three_substring)
        # List to store good size 3 substrings
        good_size_three_substrings = []  
        # Check each size 3 substring for goodness
        for substring in size_three_substrings:
            # Dictionary to track letters in the substring
            letter_tracker = {}  
            is_good_substring = True
            # Iterate over each letter in the substring
            for letter in substring:
                if letter in letter_tracker:
                    # If the letter is already in the tracker, it's not a good substring
                    is_good_substring = False
                else:
                    # Add the letter to the tracker
                    letter_tracker[letter] = 0  
            if is_good_substring:
                # If the substring is good, add it to the list of good substrings
                good_size_three_substrings.append(substring)
        # Return the count of good substrings
        return len(good_size_three_substrings)  

solution = Solution()
answer = solution.countGoodSubstrings("aababcabc")
print(answer)