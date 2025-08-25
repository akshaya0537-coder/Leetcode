class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        return[sum(nums)-sum(set(nums)),sum(range(1,n+1))-sum(set(nums))]
        nums=[1,2,2,4]
