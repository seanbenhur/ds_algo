"""Given a list of integers nums, find the most frequently occurring element and return the number of occurrences of that element.

Constraints

    0 ≤ n ≤ 100,000 where n is the length of nums

Problem Link: https://binarysearch.com/problems/High-Frequency

"""

from collections import Counter 

class Solution:
    def solve(self, nums):
        if len(nums)==0:
            return 0

        cnt = Counter(nums)
        res = []
        for key, value in cnt.items():
            res.append(value)

        return max(res)