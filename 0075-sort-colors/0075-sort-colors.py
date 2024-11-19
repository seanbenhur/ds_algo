class Solution:
    # def sortColors(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     zeroes,ones,twos = 0,0,0
        
    #     for i in range(len(nums)):
    #         if nums[i] == 0:
    #             zeroes += 1

    #         elif nums[i] == 1:
    #             ones += 1

    #         elif nums[i] == 2:
    #             twos += 1

    #     # for zero in range(zeroes-1):            
    #     #     nums[zero] = 0

        
    #     for one in range(zeroes,(ones)):
    #         print("nums[one]",nums[one])
    #         nums[one] = 1

    #     for two in range((zeroes+ones),twos-1):
    #         nums[two] = 2

#     def sortColors(self, nums) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         print("INPUT NUMS",nums)
#         zeroes,ones,twos = 0,0,0
        
#         for i in range(len(nums)):
#             if nums[i] == 0:
#                 zeroes += 1

#             elif nums[i] == 1:
#                 ones += 1

#             elif nums[i] == 2:
#                 twos += 1

#         print(f"ZEROES{zeroes}, ONES{ones} AND TWOS{twos}")
#         for zero in range(zeroes-1):            
#             nums[zero] = 0
        
#         loop_ones = ones-1
#         for one in range(zeroes,(len(nums)-1)-loop_ones):
#             nums[one] = 1


#         start_iter = zeroes+ones
#         iter = len(nums)
#         for two in range(start_iter,iter):
#           print("2nd index",two)
#           print("nums[two]",nums[two])
#           nums[two] = 2

#         print(f"FINAL ANSWER: {nums}")


# # class Solution:
#     def sortColors(self, nums) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         print("INPUT NUMS",nums)
#         zeroes,ones,twos = 0,0,0
#         loop_ones = ones-1
        
#         for i in range(len(nums)):
#             if nums[i] == 0:
#                 zeroes += 1

#             elif nums[i] == 1:
#                 ones += 1

#             elif nums[i] == 2:
#                 twos += 1

#         print(f"ZEROES{zeroes}, ONES{ones} AND TWOS{twos}")
#         for zero in range(zeroes):            
#             #print("nums[zero]",nums[zero])
#             nums[zero] = 0
        
        
#         start_iter = zeroes
#         for one in range(start_iter,(len(nums)-1)-loop_ones):
#             nums[one] = 1


#         start_iter = zeroes+ones
#         end_iter = len(nums)
#         for two in range(start_iter,end_iter):
#           print("2nd index",two)
#           print("nums[two]",nums[two])
#           nums[two] = 2

#         print(f"FINAL ANSWER: {nums}")

    def sortColors(self, nums) -> None:
        low,mid,high = 0,0,len(nums)-1

        while mid<=high:
            if nums[mid] == 0:
                nums[low],nums[mid] = nums[mid],nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid],nums[high] = nums[high], nums[mid]
                high -= 1

            
        
                
        