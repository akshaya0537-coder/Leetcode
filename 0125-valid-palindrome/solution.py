class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=''
        for ch in s:
            if(ch.isalnum()):
                t+=ch.lower()

        r=t[::-1]
        if(r==t):
            return True
        else:
            return False           

    

