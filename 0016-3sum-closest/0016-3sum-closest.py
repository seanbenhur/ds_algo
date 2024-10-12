class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('inf')

        for i in range(len(nums)-1):
            left, right = i+1, len(nums) - 1

            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]

                if three_sum == target:
                    return three_sum

                elif abs(target-three_sum)< diff:
                    diff = abs(target-three_sum)
                    ans = three_sum
                
                if three_sum < target:
                    left += 1
                else:
                    right -= 1

        return ans