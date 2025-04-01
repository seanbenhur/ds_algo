class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freq = [[] for _ in range(len(nums)+1)]
        

        # store all the keys and vals
        for key,val in counter.items():
            freq[val].append(key)

        res = []
        print("FREQS BEFORE LOOP",freq)
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

