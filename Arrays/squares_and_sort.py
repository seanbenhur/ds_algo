"""Easy

Given a list of integers sorted in ascending order nums, square the elements and give the output in sorted order."""

#Using Basic method

def solve(nums):
    nums = [i**2 for i in nums]
    return sorted(nums)


if __name__ == "__main__":
    print("Using Basic Method!")
    nums = list(map(int, input().split()))
    print(solve(nums))