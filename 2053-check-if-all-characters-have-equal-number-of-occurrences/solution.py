class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d=dict()
        for ch in s:
            if ch in d:
                d[ch]+=1
            else:
                d[ch]=1    
        if len(set(d.values()))==1:
             return True
        else:
             return False                     
