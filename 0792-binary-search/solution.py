class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        beg=0
        end=n-1
        while beg<=end:
            mid=(beg+end)//2
            if nums[mid]==target:
                return mid
            elif target<nums[mid]:
                end=mid-1
            else:
                beg=mid+1
        return -1
