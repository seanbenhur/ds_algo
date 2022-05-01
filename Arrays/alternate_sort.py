"""Alternate sorting: Given an array of integers, rearrange the array in such a way that the first 
element is first maximum and second element is first minimum. 
 
 Eg.) Input : {1, 2, 3, 4, 5, 6, 7}
 Output : {7, 1, 6, 2, 5, 3, 4}"""


def alternate_sort(nums):
    nums.sort()
    i, j = 0, len(nums)-1
    while i < j:
        
        print(nums[j], end= ', ')
        j -= 1
        print(nums[i], end= ', ')
        i += 1


if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    alternate_sort(nums)




