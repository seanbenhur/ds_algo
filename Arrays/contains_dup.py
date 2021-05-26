"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct."""


def containsDuplicate(nums):
        return len(set(nums))!=len(nums)


if __name__ == "__main__":
    nums = list(map(int,input().split()))
    print(containsDuplicate(nums))