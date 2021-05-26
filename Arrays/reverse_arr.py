
def reverse_arr(nums):
    return nums[::-1]


if __name__ == "__main__":
    nums = list(map(int,input().split()))
    rev_nums = reverse_arr(nums)
    print(rev_nums)