class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        res = 0
        
        for right in range(len(s)):
            while s[right] in char_set:
                #if the char is already in the set remove the left most char
                char_set.remove(s[left])
                #move the left pointer
                left += 1
            #add the charcter to set
            char_set.add(s[right])
            #+1 is used since index starts from 0
            res = max(res,(right-left)+1)
        return res
            
            
        