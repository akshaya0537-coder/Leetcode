class Solution:
    def largestNumber(self, nums: List[int]) -> str:
         # Convert integers to strings
        str_nums = [str(num) for num in nums]

        # Custom comparison function
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1  # n1 should come before n2
            elif n1 + n2 < n2 + n1:
                return 1   # n2 should come before n1
            else:
                return 0   # Order doesn't matter

        # Sort using the custom comparison
        str_nums.sort(key=cmp_to_key(compare))

        # Handle the edge case of all zeros
        if str_nums[0] == '0':
            return '0'

        # Join the sorted strings
        return "".join(str_nums)
