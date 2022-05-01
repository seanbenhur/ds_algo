class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        res = []
        j = len(res)-1
        
        for i,c in enumerate(s):
            if c.isalpha():
                while not s[j].isalpha():
                    j -= 1
                res.append(s[j])
                j -= 1
            else:
                res.append(c)
                
        return ''.join(res)

                
                
        
                
            
        