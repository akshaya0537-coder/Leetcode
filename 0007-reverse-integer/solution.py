class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        if x < 0:
            is_negative = True
            x = abs(x)

        reversed_num = 0
        while x > 0:
            digit = x % 10
            reversed_num = (reversed_num * 10) + digit
            x //= 10

        # Check for overflow (32-bit signed integer range)
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if reversed_num > INT_MAX or (is_negative and -reversed_num < INT_MIN):
            return 0

        return -reversed_num if is_negative else reversed_num

