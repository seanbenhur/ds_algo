class Solution:
    def searchRange(self, nums, target: int):
        def binarysearchleft(nums, target):
            left = 0
            right = len(nums) - 1
            index = -1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid
                    right = mid - 1  # Search left side for first occurrence
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return index

        def binarysearchright(nums, target):
            left = 0
            right = len(nums) - 1
            index = -1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid
                    left = mid + 1  # Search right side for last occurrence
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return index

        return [binarysearchleft(nums, target), binarysearchright(nums, target)]
