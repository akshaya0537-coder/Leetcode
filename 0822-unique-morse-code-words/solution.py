class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mcode=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res=[]
        for word in words:
            str1=""
            for ch in word:
                str1+=mcode[ord(ch)-97]
            res.append(str1)
        s1=set(res)
        return len(s1)
