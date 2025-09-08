class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for num in nums:
            if num==0:
                nums.remove(num)
                nums.append(num)
        """
        Do not return anything, modify nums in-place instead.
        """
        
