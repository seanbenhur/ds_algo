class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in nums:
                next_num = num+1
                while next_num in nums:
                    next_num += 1
                longest = max(longest,next_num-num)
        return longest
            
        