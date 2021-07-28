"""Given a list of integers nums sorted in ascending order, remove in-place duplicates that appear more than twice.

This should be done in O(1)\mathcal{O}(1)O(1) space.

Constraints

    n ≤ 100,000 where n is the length of nums

"""


class Solution:
    def solve(self, nums):
        if len(nums)<3:
            return nums

        i = 2
        while i<len(nums):
            if nums[i] == nums[i-2]:
                nums.pop(i)
            else:
                i += 1
        return nums

        
        