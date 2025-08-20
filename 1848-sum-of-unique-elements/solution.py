class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        ans =0
        d =dict()
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        for K,V in d.items():
                    if V==1:
                        ans+=K
        return ans
        
