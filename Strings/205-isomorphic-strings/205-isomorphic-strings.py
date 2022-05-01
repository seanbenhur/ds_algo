class Solution:
    def transform(self,s):
        #create a hashmap
        index = {}
        new = []
        
        for i,c in enumerate(s):
            if c not in index:
                index[c]=i
            new.append(str(index[c]))
        
        return " ".join(new)
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.transform(s)==self.transform(t)
        
        