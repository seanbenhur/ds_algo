class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set) #key = row_index
        cols = collections.defaultdict(set) #key=col_index
        squares = collections.defaultdict(set) #key=(row_index/3, col_index/3)
        
        for row in range(9):
            for col in range(9):
                
                if board[row][col] == '.':
                    continue
                
                if(board[row][col] in rows[row] or 
                    board[row][col] in cols[col] or
                    board[row][col] in squares[(row//3,col//3)]):
                        
                        return False
                
                cols[col].add(board[row][col])
                rows[row].add(board[row][col])
                squares[(row // 3, col // 3)].add(board[row][col])
        return True        
        