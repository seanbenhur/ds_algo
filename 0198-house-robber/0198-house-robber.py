class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        if not nums:
            return 0

        nums[1] = max(nums[0],nums[1])
    
        for i in range(2,len(nums)):
            nums[i] = nums[i]+nums[i-2]
            print(nums[i])

        return max(nums[i],nums[i-1])




            


# 1st iteration - 100, 10, 101, 10, 100

# 1st iteration - 100, 10, 101, 10, 100

#

# 1st iteration - [2,7,11,3,1]
# 2st iteration - [2,7,11,10,1]
