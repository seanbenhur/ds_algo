class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        columns = set()
        pos_diag = set() #(row+col) - bottom to top diagonal
        neg_diag = set() #(row-col) - top to bottom diagonal
        
        result = []
        board = [['.'] * n for i in range(n)]
        
        def backtrack(row):
            #Parameter : 
            #row: each row of the board
            if row==n:
                #we are iterating 
                copy = [''.join(row) for row in board]
                result.append(copy)
                return 
            
            for col in range(n):
                if col in columns or (row+col) in pos_diag or (row-col) in neg_diag:
                    continue
                
                columns.add(col)
                pos_diag.add(row+col)
                neg_diag.add(row-col)
                board[row][col] = 'Q'
                
                #iterate to next row
                backtrack(row+1)
                
                #remove all the values, since we have to start from new values
                columns.remove(col)
                pos_diag.remove(row+col)
                neg_diag.remove(row-col)
                board[row][col] = '.'
        backtrack(0)
        return result
        
        
        
        