class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        oddsum,evensum=0,0
        for i in range(len(nums)):
            if i%2==0:
                evensum+=nums[i]
            else:
                oddsum+=nums[i]
        return evensum-oddsum
