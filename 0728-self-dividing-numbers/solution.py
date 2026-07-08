class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def snum(n:int)->bool:
            count=0
            for d in str(n):
                if int(d)!=0:
                    if n%(int(d))==0:
                        count+=1
            if count==len(str(n)):
                return True
            else:
                return False
        res=[]
        for i in range(left,right+1):
            if snum(i)==True:
                res.append(i)
        return res
