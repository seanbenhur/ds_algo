class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        index = 1
        n = len(nums)
        for i in range(n-1):
            if nums[i]!=nums[i+1]:
                nums[index]=nums[i+1]
                index += 1
        return index