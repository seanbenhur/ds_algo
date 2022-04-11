class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        vector = [0]*rows*cols
        k = k%(rows*cols)
        
        for i in range(rows):
            for j in range(cols):
                vector[i*cols+j] = grid[i][j]
                
        self.reverse(vector,0,rows*cols-1)
        self.reverse(vector,0,k-1)
        self.reverse(vector,k,rows*cols-1)
        
        for i in range(rows):
            for j in range(cols):
                grid[i][j] = vector[i*cols+j]
        
        return grid
    
    def reverse(self,nums,start,end):
        while start < end:
            nums[start],nums[end] = nums[end],nums[start]
            start+=1
            end-=1