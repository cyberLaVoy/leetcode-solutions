class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        test_string = s
        valid_with_rotations = False
        for _ in range(len(s)):
            if test_string == goal:
                valid_with_rotations = True
                break
            # Rotation operation
            test_string = test_string[1:len(test_string)] + test_string[0]
        return valid_with_rotations