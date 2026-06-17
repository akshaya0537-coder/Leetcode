class Solution:
    def maxDepth(self, s: str) -> int:
        
        count=0
        maxcount=0
        stack=[]
        for ch in s:
            if ch=="(":
                stack.append(ch)
                count+=1
            elif ch==")":
                if count>maxcount:
                    maxcount=count
                count-=1
                stack.pop()
        return maxcount
