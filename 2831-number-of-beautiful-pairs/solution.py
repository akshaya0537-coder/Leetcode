import math
from typing import List

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)

        def get_first_digit(num):
            while num >= 10:
                num //= 10
            return num

        for i in range(n):
            first_digit_i = get_first_digit(nums[i])
            for j in range(i + 1, n):
                last_digit_j = nums[j] % 10
                if math.gcd(first_digit_i, last_digit_j) == 1:
                    count += 1

        return count
