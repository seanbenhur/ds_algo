class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reflect(matrix)
    
    def transpose(self,matrix):
        for i in range(len(matrix[0])):
            for j in range(i+1,len(matrix[0])):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    
    def reflect(self,matrix):
        """To reverse the column of the transposed matrix, run two nested loops, the outer loop from 0 to column count and the inner loop from 0 to row count/2, interchange elements at (i, j) with (i, row[count-1-j]), where i and j are indices of inner and outer loop respectively."""
        for i in range(len(matrix[0])):
            for j in range(len(matrix[0])//2):
                matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]
                