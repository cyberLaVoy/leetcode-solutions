class Solution:
    def isHappy(self, n: int) -> bool:
        is_happy = False
        operation_history = []
        sum_of_digits_squares = sum([int(v)**2 for v in str(n)])
        while True:
            if sum_of_digits_squares in operation_history:
                break
            operation_history.append(sum_of_digits_squares)
            if sum_of_digits_squares == 1:
                is_happy = True
                break
            sum_of_digits_squares = sum([int(v)**2 for v in str(sum_of_digits_squares)])
        return is_happy