class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 100,4,1,3,2
        1,2,3,4,100
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1

        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num-1 not in num_set:
                current_num = num
                current_streak = 1 

                while current_num + 1 in num_set:
                    current_streak += 1
                    current_num += 1
                longest = max(current_streak,longest)
        return longest

# current_num = 1
# current_streak = 2
# # 100,4,200,1,3,2

# longest = 1

