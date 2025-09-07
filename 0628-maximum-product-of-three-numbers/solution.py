class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()  # Sort the array in ascending order
        n = len(nums)

        # Product of the three largest numbers
        product1 = nums[n - 1] * nums[n - 2] * nums[n - 3]

        # Product of the two smallest numbers and the largest number
        product2 = nums[0] * nums[1] * nums[n - 1]

        return max(product1, product2)
