class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evenlist=[]
        oddlist=[]
        for num in nums:
            if num%2==0:
                evenlist.append(num)
            else:
                oddlist.append(num)
        return evenlist+oddlist
