"""Given a string s and an integer k, return the number of k-length substrings that occur more than once in s.

Constraints

    n ≤ 100,000 where n is the length of s.
    k ≤ 10

"""

from collections import Counter

class Solution:
    def solve(self, s, k):
        cnt = Counter()

        for i in range(k,len(s)+1):
            cnt[s[i-k:i]] += 1

        res = 0
        for i in cnt:
            if cnt[i]>1:
                res +=1
        return res
        


        

