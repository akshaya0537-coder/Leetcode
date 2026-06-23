class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        max_area = 0

        for i in range(len(heights) + 1):

            
            if i == len(heights):
               curr_height = 0
            else:
               curr_height = heights[i]

            while stack and curr_height < heights[stack[-1]]:
                h = heights[stack.pop()]

                if stack:
                    left = stack[-1]
                else:
                    left = -1

                width = i - left - 1
                area = h * width

                max_area = max(max_area, area)

            stack.append(i)

        return max_area
        
