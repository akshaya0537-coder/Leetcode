class Solution:
    def countDigits(self, num: int) -> int:
        a=str(num)
        count=0
        for i in a:
            if num%int(i)==0:
                count+=1
        return count        
