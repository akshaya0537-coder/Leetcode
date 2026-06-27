class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length=float('inf')
        cur_sum=0
        l=0
        for r in range(len(nums)):
            cur_sum+=nums[r]
            while cur_sum>=target:
                min_length=min(min_length,r-l+1)
                cur_sum-=nums[l]
                l+=1
        return min_length if min_length!=float('inf')else 0
