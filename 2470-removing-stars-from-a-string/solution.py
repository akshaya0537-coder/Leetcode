class Solution:
    def removeStars(self, s: str) -> str:
        t=[]
        for ch in s:
            if ch=='*':
                t.pop()
            else:
                t.append(ch)
        return"".join(t)
