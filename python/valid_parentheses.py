class Solution:
    def isValid(self, s: str) -> bool:
        """
        Checks whether a string containing only parentheses, brackets, and/or curly braces is balanced.
        A string is balanced if every opening bracket has a corresponding closing bracket in the correct order.
        :param s: The string to check.
        :return: True if the string is balanced, False otherwise.
        """
        # Define a dictionary with opening and closing bracket pairs.
        bracket_match = {
            '(':')',
            '{':'}',
            '[':']'
        }
        
        # Create a stack to keep track of opening brackets.
        stack = []
        
        # Initialize a boolean variable to keep track of whether the string is valid.
        is_valid = True
        
        # Loop through each symbol in the string.
        for symbol in s:
            # If the symbol is an opening bracket, add it to the stack.
            if symbol in bracket_match.keys():
                stack.append(symbol)
            # If the symbol is a closing bracket, check if it matches the most recent opening bracket.
            elif symbol in bracket_match.values():
                # If there are no opening brackets on the stack, the string is invalid.
                if len(stack) == 0:
                    is_valid = False
                    break
                # Otherwise, pop the most recent opening bracket from the stack and check if the closing bracket matches.
                popped_symbol = stack.pop()
                if bracket_match[popped_symbol] != symbol:
                    is_valid = False
                    break
        
        # If there are any remaining opening brackets on the stack, the string is invalid.
        if len(stack) != 0:
            is_valid = False
        
        # Return whether the string is valid.
        return is_valid