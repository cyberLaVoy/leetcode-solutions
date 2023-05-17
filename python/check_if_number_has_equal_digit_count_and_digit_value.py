class Solution:
    def digitCount(self, num: str) -> bool:
        count_tracker = {}
        for i in range(len(num)):
            count_tracker[str(i)] = 0
        for digit in num:
            if digit not in count_tracker.keys():
                count_tracker[digit] = 1
            else:
                count_tracker[digit] += 1
        has_equal_digit_count_and_index_value = True
        # check if the index i occurs num[i] times in num
        for i in range(len(num)):
            if count_tracker[str(i)] != int(num[i]):
                has_equal_digit_count_and_index_value = False
                break
        return has_equal_digit_count_and_index_value