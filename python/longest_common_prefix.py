class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """
        This function takes in a list of strings and returns the longest common prefix among them.
        If there is no common prefix, an empty string is returned.
        
        Args:
        - strs: A list of strings
        
        Returns:
        - str: The longest common prefix among the strings in the input list
        """

        # Determine the length of the shortest string in the list.
        shortest_word_length = min([len(word) for word in strs])
        
        # Generate a list of all possible prefixes for each string up to the length of the shortest string.
        prefixes = []
        for i in range(shortest_word_length+1):
            sub_prefixes = []
            for word in strs:
                sub_prefixes.append(word[0:i])
            prefixes.append(sub_prefixes)

        # Iterate through each list of prefixes to find the longest common prefix among them.
        longest_prefix = ""
        for sub_prefixes in prefixes:
            prefix_check = sub_prefixes[0]
            all_match = True
            for i in range(1, len(sub_prefixes)):
                if prefix_check != sub_prefixes[i]:
                    all_match = False
            if all_match and len(prefix_check) > len(longest_prefix):
                longest_prefix = prefix_check

        return longest_prefix



