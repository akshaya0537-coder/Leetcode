class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=[]
        for symbol in operations:
            if symbol=="+":
                res.append(res[-1]+res[-2])
            elif symbol=="D":
                res.append(res[-1]*2)
            elif symbol=="C":
                res.pop()
            else:
                res.append(int(symbol))
        return sum(res)
