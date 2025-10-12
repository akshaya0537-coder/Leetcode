class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n == 0:
            return 0

        # Sort by end time
        intervals.sort(key=lambda x: x[1])

        count = 1  # number of non-overlapping intervals
        end = intervals[0][1]

        for i in range(1, n):
            if intervals[i][0] >= end:
                end = intervals[i][1]
                count += 1

        # intervals to remove = total - non-overlapping
        return n - count

