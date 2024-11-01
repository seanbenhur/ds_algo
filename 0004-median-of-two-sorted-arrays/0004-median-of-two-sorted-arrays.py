class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2,nums1

        m , n = len(nums1), len(nums2)

        left, right =0, m
        total = m + n
        half = total / 2

        while left <= right:
            i = (left+right)//2
            j = (m+n+1) // 2 - i

            max_left_1 = nums1[i - 1] if i > 0 else float('-infinity')
            min_right_1 = nums1[i] if i < m else float('infinity')

            max_left_2 = nums2[j-1] if j > 0 else float('-infinity')
            min_right_2 = nums2[j] if j < n else float('infinity')

            if max_left_1 <= min_right_2 and max_left_2 <= min_right_1:
                if (m + n)%2 == 0:
                    return (max(max_left_1,max_left_2) + min(min_right_1,min_right_2))/2
                else:
                    return max(max_left_1,max_left_2)

            if max_left_1 > min_right_2:
                right = i -1
            else:
                left = i + 1
