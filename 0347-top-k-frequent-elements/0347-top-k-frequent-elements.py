class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        heap = []

        for num in nums:
            counter[num] = 1 + counter.get(num,0)

        for key, val in counter.items():
            heapq.heappush(heap, (-val,key))

        res = []

        while len(res) < k:
            res.append(heapq.heappop(heap)[1])

        return res

        
