class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq=dict()
        for num in arr:
            if num not in freq:
                freq[num]=1
            else:
                freq[num]=freq[num]+1
        result=[-1]
        for (k,v) in freq.items():
            if(k==v):
                result.append(k)
        return max(result)
        
