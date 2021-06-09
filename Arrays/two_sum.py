"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice."""



def twoSumLoops(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                 return [i,j]

def twoSumHash(nums,target):
    d = {}
    for  i,n in enumerate(nums):
        m = target - n
        if m in d:
            return [d[m], i]
        else:
            return [d[n], i]

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    target = input()
    print("Using Loops")
    print(twoSumLoops(nums,target))
    print("Using Hashmap")
    print(twoSumHash(nums,target))