"""Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?"""

def missing_number_hash(nums):
    numset = set(nums)
    for i in range(len(nums)+1):
        if i not in nums:
            return i


def missing_number_gauss(nums):
    n = len(nums)
    return n*(n+1)//2 - sum(nums)


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print("Using Hashmap!!")
    print(missing_number_hash(nums))
    print("Using Gauss Formula!!")
    print(missing_number_gauss(nums))