"""Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array."""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best_sum = nums[0]
        curr_sum = nums[0]
        
        for num in range(1,len(nums)):
            curr_sum = max(nums[num], curr_sum+nums[num])
            best_sum = max(best_sum,curr_sum)
        return best_sum