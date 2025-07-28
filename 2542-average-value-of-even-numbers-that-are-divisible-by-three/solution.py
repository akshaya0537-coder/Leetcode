class Solution:
    def averageValue(self, nums: List[int]) -> int:
        count=0
        sum1=0
        for num in nums:
            if num%6==0:
                sum1+=num
                count+=1
        if sum1==0:
            return 0
        else:
            return sum1//count
