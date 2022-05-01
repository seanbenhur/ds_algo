class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        freqs = [[] for _ in range(len(nums)+1)]
        
        for key,freq in counts.items():
            freqs[freq].append(key)
            
        res = []
        
        for i in range(len(freqs)-1,-1,-1):
            for n in freqs[i]:
                res.append(n)
                if len(res)==k:
                    return res
            
        