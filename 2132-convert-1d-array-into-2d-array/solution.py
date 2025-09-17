class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        l=len(original)
        k=0
        matrix1=[]
        if l!=m*n:
            return matrix1
        for i in range(m):
            row=[]
            for j in range(n):
                row.append(original[k])
                k+=1
            matrix1.append(row)
        return matrix1
        
