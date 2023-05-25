class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Adds two binary numbers represented as strings and returns the sum as a binary string.

        Args:
            a (str): The first binary number.
            b (str): The second binary number.

        Returns:
            str: The sum of the binary numbers.

        Example:
            >>> solution = Solution()
            >>> solution.addBinary("1010", "1011")
            '10101'
        """

        # Convert the binary numbers to their integer representation and add them
        integer_summation = 0
        for i in range(len(a)):
            if a[len(a) - 1 - i] == '1':
                integer_summation += 2 ** i
        for i in range(len(b)):
            if b[len(b) - 1 - i] == '1':
                integer_summation += 2 ** i

        # Convert the sum back to binary representation
        binary_summation = []
        temp_integer_summation = integer_summation
        while temp_integer_summation != 0:
            if temp_integer_summation % 2 == 1:
                binary_summation.append("1")
            else:
                binary_summation.append("0")
            temp_integer_summation = temp_integer_summation // 2

        # Reverse the binary digits and convert the list to a string
        binary_summation.reverse()
        binary_summation = ''.join(binary_summation)

        # If the sum is an empty string, set it to '0'
        if binary_summation == "":
            binary_summation = "0"

        return binary_summation


solution = Solution()
example1 = solution.addBinary("1010", "1011")
print(example1)