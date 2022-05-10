class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        count_t, window = {}, {}
        
        for char in t:
            count_t[char] = count_t.get(char,0) + 1
        
        have, need = 0, len(count_t)
        res, reslen = [-1,-1], float('inf')
        
        l = 0
        for r,char in enumerate((s)):
            window[char] = 1 + window.get(char,0)
            
            if char in count_t and window[char]==count_t[char]:
                have += 1
                
            while have == need:
                if (r-l+1) < reslen:
                    res = [l,r]
                    reslen = r-l+1
                    
                #pop left
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        l,r = res
        return s[l:r+1] if reslen!=float('inf') else ""
        
        
            
                  