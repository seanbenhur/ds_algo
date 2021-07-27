"""Given two lists of integers a and b sorted in ascending order, merge them into one large sorted list.

Constraints

    0 ≤ n ≤ 200,000 where n is the length of a
    0 ≤ m ≤ 200,000 where m is the length of b

"""


class Solution:
    def solve(self, a, b):
        start, end, result = 0, 0 ,[]
        while start < len(a) and end < len(b):
            if a[start]<=b[end]:
                result.append(a[start])
                start += 1
            else:
                result.append(b[end])
                end += 1
        return result + a[start:] + b[end:]