class Solution:
    def topKFrequent(self, nums, k: int):
        count_dict = Counter(nums)
        keys = count_dict.most_common(k)
        res = [k for k,v in keys]
        print(res)
        return res