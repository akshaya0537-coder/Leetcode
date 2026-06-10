class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d={}
        for index,val in enumerate(sorted(nums)):
            if val not in d:
                d[val]=index
        ans=[d[val] for val in nums]
        return ans
