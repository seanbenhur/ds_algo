class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
            
        l = 0
        char_set = set()
        maxlen = 0


        # loop from r 
        for r in range(len(s)):
            # if rth string remains in the set
            while s[r] in char_set:
                # remove the left and update it by 1
                char_set.remove(s[l])
                l += 1
            
            char_set.add(s[r])
            maxlen = max(maxlen,r-l+1)
        return maxlen

        