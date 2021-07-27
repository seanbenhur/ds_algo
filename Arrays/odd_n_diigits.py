"""Given a list of positive integers nums, return the number of integers that have odd number of digits.

Constraints

    n ≤ 100,000 where n is the length of nums

"""


class Solution:
    def solve(self, nums):
        count = 0
        for num in nums:
            if len(str(num))%2 != 0:
                count += 1
        return count
