



"""def find_min(nums):
    nums.sort()
    return nums[0]"""

"""def find_max(nums):
    nums.sort()
    return nums[-1]"""


if __name__ == "__main__":
    nums = list(map(int,input().split()))
    min = find_min(nums)
    max = find_max(nums)
    print(min,max)