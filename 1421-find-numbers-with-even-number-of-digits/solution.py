class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_digit_count = 0
        for num in nums:
            # Convert to string and get length
            digit_count = len(str(num))
            
            # Check if the digit count is even
            if digit_count % 2 == 0:
                even_digit_count += 1
        return even_digit_count
