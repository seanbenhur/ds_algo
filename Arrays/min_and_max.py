"""Find minimum and maximum element without sort method"""



def find_min_loop(nums):
    temp = nums[0]
    for i in range(len(nums)):
        if nums[i]<temp:
            min =  nums[i]
    return min

def find_max_loop(nums):
    temp = nums[0]
    for i in range(len(nums)):
        if nums[i]>temp:
            max = nums[i]
    return max


if __name__ == "__main__":
    nums = list(map(int,input().split()))
    print(find_min_loop(nums))
    print(find_max_loop(nums))