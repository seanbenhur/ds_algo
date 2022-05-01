"""Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.


Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:
Input: nums = [1], k = 1
Output: [1]"""
 
from collections import Counter 
from typing import List



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]
        for key, val in counts.items():
            freq[val].append(key)
    
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
            
        
sol = Solution()
nums = [3,0,1,0]
k=1
print(sol.topKFrequent(nums,k))