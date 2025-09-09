class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) ^ (divisor < 0)
        dvd, dvs = abs(dividend), abs(divisor)
        result = 0

        while dvd >= dvs:
            temp, multiple = dvs, 1
            while dvd >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dvd -= temp
            result += multiple

        if negative:
            result = -result
        return min(max(result, INT_MIN), INT_MAX)

