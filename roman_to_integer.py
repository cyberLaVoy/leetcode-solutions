class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Convert a Roman numeral string to an integer.

        Parameters:
        s (str): The Roman numeral string to be converted.

        Returns:
        int: The integer representation of the Roman numeral string.

        """
        # Define a dictionary of Roman numeral symbols and their integer values.
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        # Initialize the integer representation of the Roman numeral string as 0.
        roman_numeral_as_integer = 0
        # Initialize the index i to 0.
        i = 0
        # While there are still Roman numeral symbols to process.
        while i < len(s):
            # If the current symbol is the last symbol in the string, add its value to the integer representation and exit the loop.
            if i == len(s)-1:
                roman_numeral_as_integer += roman_numerals[ s[i] ]
                break
            # If the current symbol is 'I' and the next symbol is 'V' or 'X', subtract the value of the current symbol from the value of the next symbol and add the result to the integer representation. 
            # Increment i by 1 to skip the next symbol.
            if s[i] == 'I' and  s[i+1] in ('V', 'X'):
                roman_numeral_as_integer += ( roman_numerals[ s[i+1] ] - roman_numerals[ s[i] ] )
                i += 1
            # If the current symbol is 'X' and the next symbol is 'L' or 'C', subtract the value of the current symbol from the value of the next symbol and add the result to the integer representation. 
            # Increment i by 1 to skip the next symbol.
            elif s[i] == 'X' and s[i+1] in ('L', 'C'):
                roman_numeral_as_integer += ( roman_numerals[ s[i+1] ] - roman_numerals[ s[i] ] )
                i += 1
            # If the current symbol is 'C' and the next symbol is 'D' or 'M', subtract the value of the current symbol from the value of the next symbol and add the result to the integer representation. 
            # Increment i by 1 to skip the next symbol.
            elif s[i] == 'C' and s[i+1] in ('D', 'M'):
                roman_numeral_as_integer += ( roman_numerals[ s[i+1] ] - roman_numerals[ s[i] ] )
                i += 1
            # Otherwise, add the value of the current symbol to the integer representation.
            else:
                roman_numeral_as_integer += roman_numerals[ s[i] ]
            # Increment i by 1 to move to the next symbol.
            i += 1
        # Return the final integer representation of the Roman numeral string.
        return roman_numeral_as_integer 

