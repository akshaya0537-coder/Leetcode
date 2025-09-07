class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_nums = [1]
        i2, i3, i5 = 0, 0, 0

        while len(ugly_nums) < n:
            next_ugly_2 = ugly_nums[i2] * 2
            next_ugly_3 = ugly_nums[i3] * 3
            next_ugly_5 = ugly_nums[i5] * 5

            next_ugly = min(next_ugly_2, next_ugly_3, next_ugly_5)

            # Increment pointers for all factors that produced the minimum
            if next_ugly == next_ugly_2:
                i2 += 1
            if next_ugly == next_ugly_3:
                i3 += 1
            if next_ugly == next_ugly_5:
                i5 += 1

            ugly_nums.append(next_ugly)

        return ugly_nums[-1]
