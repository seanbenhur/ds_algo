class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums)<=2:
            return nums.index(max(nums))
        left,right=0,len(nums)-1
        
        while left<=right:
            mid = (left+right)//2
            if nums[mid]<nums[mid-1]:
                right = mid-1
            else:
                left = mid+1
        return right
        