class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [
            sum(1 for i in nums1 if i in nums2),
            sum(1 for i in nums2 if i in nums1)
        ]
