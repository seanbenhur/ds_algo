class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarysearchright(nums,x):
            left, right = 0, len(nums)-1
            index = -1
            while left<=right:
                mid = (left + right)//2
                
                if nums[mid]==x:
                    index = mid
                    left = mid+1
                elif nums[mid] < x:
                    left = mid+1
                else:
                    right = mid-1
            return index
        
                    
        def binarysearchleft(nums,x):
            left,right = 0, len(nums)-1
            index = -1
            while left<=right:
                mid = (left + right)//2
                if nums[mid]==x:
                    index = mid
                    right=mid-1
                elif nums[mid]<x:
                    left = mid+1
                else:
                    right = mid-1
            return index
        
        
        return [binarysearchleft(nums,target),binarysearchright(nums,target)]
                    
                
        