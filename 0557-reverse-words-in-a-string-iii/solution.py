class Solution:
    def reverseWords(self, s: str) -> str:
        result=[]
        list1=s.split()
        for word in list1:
            result.append(word[::-1])
        return " ".join(result)
