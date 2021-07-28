"""Given a list of integers nums, put all the zeros to the back of the list by modifying the list in-place. The relative ordering of other elements should stay the same.

Can you do it in O(1)\mathcal{O}(1)O(1) additional space?

Constraints

    0 ≤ n ≤ 100,000 where n is the length of nums

"""


class Solution:
    def solve(self, nums):
       res = 0
       for i in range(len(nums)):
           if nums[i]!=0:
               nums[res], nums[i] = nums[i],nums[res]
               res += 1
       return nums