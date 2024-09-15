class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        left,right = min(bloomDay), max(bloomDay)

        while left < right:
            mid = (left + right) // 2
            if feasibility(bloomDay,mid,m,k):
                right = mid
            else:
                left = mid + 1
        return left


def feasibility(nums,day,m,k):
    count = 0
    n_bouq = 0
    for num in nums:
        if num <= day:
            count += 1
            if count == k:
                n_bouq += 1
                count = 0
        else:
            count= 0
    return n_bouq >= m





    