"""Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space."""


class Solution(object):
    """Solution using Floyd's Warshall Algorithm"""
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        slow, fast = nums[0], nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow==fast:
                break
                
        slow = nums[0]
        
        while slow!=fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return fast



                
        
            