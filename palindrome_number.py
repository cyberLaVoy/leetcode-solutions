class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Determines whether an input integer is a palindrome.
        Args:
            x: An integer to check for palindrome-ness.
        Returns:
            True if x is a palindrome, False otherwise.
        """
        # Convert the input integer to a string for easier comparison.
        x_as_string = str(x)
        # Initialize a boolean variable to keep track of whether x is a palindrome.
        is_palindrome = True
        # Iterate through each character in the string representation of x.
        for i in range(len(x_as_string)):
            # Compare the i-th character with the (len(x_as_string)-i-1)-th character,
            # which represents the corresponding character from the end of the string.
            if x_as_string[i] != x_as_string[len(x_as_string)-i-1]:
                # If any pair of characters don't match, then x is not a palindrome.
                is_palindrome = False
        # Return whether x is a palindrome.
        return is_palindrome