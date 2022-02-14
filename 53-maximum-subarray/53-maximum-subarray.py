class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        local_max = nums[0]
        global_max = nums[0]
        
        
        for i in range(1,len(nums)):
            current = nums[i]
            local_max = max(current,local_max+current)
            global_max = max(local_max,global_max)
        return global_max