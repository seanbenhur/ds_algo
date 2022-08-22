def reverse(digit):
    res, x_remaining = 0, abs(digit)
    while x_remaining:
        res = res* 10 + x_remaining %10
        x_remaining = x_remaining // 10
    return -res if digit < 0 else res


if __name__ == "__main__":
    digit = 124
    rev = reverse(digit)
    print(rev)