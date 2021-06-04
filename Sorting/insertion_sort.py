"""Implementation of insertion sort in Python"""


def insertion_sort(nums):
    #loop through all except first element in the list
    for index in range(1,len(nums)):
        value = nums[index]

        position = index - 1

        #insert the key in correct place
        while position >= 0 and nums[position] > value:
            nums[position+1] = nums[position]
            position -= 1

        nums[position + 1] = value
    
    return nums
    



if __name__ == "__main__":
    unsorted = list(map(int,input().split()))
    sorted = insertion_sort(unsorted)
    print(sorted)