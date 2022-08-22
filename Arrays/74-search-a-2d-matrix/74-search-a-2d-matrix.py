class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #if there is no matrix, return False
        if not matrix or not matrix[0]: return False
        #find the shape of the rows and cols
        m, n = len(matrix[0]), len(matrix)
        #m*n -> is the shape of the whole matrix, for example, to acces the last element in a 3*3 matrix,
        #3*3 - 1 = 8
        left, right = 0, m*n - 1
        
        while left < right:
            mid = (left+right)//2
            
            if matrix[mid//m][mid%m] < target:
                left = mid+1
            else:
                right = mid
        
        return matrix[left//m][right%m] == target 