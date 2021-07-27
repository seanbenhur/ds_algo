"""Given an integer n, return whether it is equal to the sum of its own digits raised to the power of the number of digits."""



class Solution:
    def solve(self, n):
        res = 0
        len_n = len(str(n))

        for i in str(n):
            res = res + int(i)**len_n

        return n == res
        