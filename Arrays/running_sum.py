"""Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums."""

import itertools

def runningSum(nums):
        sumList = []
        total = 0
        
        for num in nums:
            total += num
            sumList.append(total)
        return sumList

            

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print("Using simple for loop")
    print(runningSum(nums))
