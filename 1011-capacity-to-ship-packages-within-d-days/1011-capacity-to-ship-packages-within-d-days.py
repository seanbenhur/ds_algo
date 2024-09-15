class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:


        left, right = max(weights), sum(weights)

        while left < right:
            mid = left + (right-left)//2
            if self.feasiblity(mid,weights,D):
                right = mid
            else:
                left = mid + 1
        return left

    def feasiblity(self,capacity,weights,D):
        
        days = 1
        total_weight = 0

        for weight in weights:
            total_weight += weight

            if total_weight > capacity:
                total_weight = weight
                days += 1

                if days > D:
                    return False
        return True


# def feasible(capacity) -> bool:
#         days = 1
#         total = 0
#         for weight in weights:
#             total += weight
#             if total > capacity:  # too heavy, wait for the next day
#                 total = weight
#                 days += 1
#                 if days > D:  # cannot ship within D days
#                     return False
#         return True

        