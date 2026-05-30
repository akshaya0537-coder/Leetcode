from itertools import permutations 
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perm=permutations(nums)
        return (list(set(perm)))
