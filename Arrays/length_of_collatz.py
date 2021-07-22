"""Given a positive integer n, find the length of its Collatz sequence. The Collatz sequence is generated sequentially where

    n = n / 2 if n is even
    n = 3 * n + 1 if n is odd
    And the sequence ends if n = 1

"""

class Solution:
    def solve(self, n):
        if n==0:
            return 0
        length = 1
        while n!=1:
            n = (n/2) if n%2==0 else (3*n+1)
            length+=1
        return length

if __name__ == "__main__":
    n = int(input())
    sol = Solution()
    ans = sol.solve(n)
    print(ans)
