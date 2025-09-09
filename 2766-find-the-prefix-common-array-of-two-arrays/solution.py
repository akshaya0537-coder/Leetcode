class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        n = len(A)
        count = [0] * (n + 1)
        prefix_common = 0
        C = []
        for a, b in zip(A, B):
            count[a] += 1
            if count[a] == 2:
                prefix_common += 1
            count[b] += 1
            if count[b] == 2:
                prefix_common += 1
            C.append(prefix_common)
        return C

