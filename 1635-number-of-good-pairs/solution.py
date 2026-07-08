class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n=len(nums)
        counter=Counter(nums)
        gp=0
        for i,num in enumerate(nums):
            counter[num]-=1
            gp=gp+counter[num]
        return gp
        
