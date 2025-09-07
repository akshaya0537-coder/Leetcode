# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid  # mid could be the first bad version, or it's earlier
            else:
                left = mid + 1 # mid is good, first bad version must be after mid
        return left # left (or right) now points to the first bad version
