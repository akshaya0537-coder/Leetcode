

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(32):  # for each bit position
            bit_sum = 0
            for num in nums:
                # Extract the ith bit of num
                bit_sum += (num >> i) & 1

            # Modulo by 3 to get the bit of the unique number
            bit_sum %= 3

            # Handle negative numbers (sign bit)
            if i == 31 and bit_sum:
                result -= (1 << i)
            else:
                result |= (bit_sum << i)

        return result

