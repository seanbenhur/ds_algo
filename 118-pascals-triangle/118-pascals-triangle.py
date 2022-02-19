class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows
        rows = [[1]* i for i in range(1,n+1)]
        
        for i in range(1,n):
            for j in range(1,i):
                rows[i][j] = rows[i-1][j] + rows[i-1][j-1]
        return rows