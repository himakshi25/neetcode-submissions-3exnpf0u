class Solution:
    def getAdjacentCells(self, i, j, rows, cols):
        """Get indices of 4 adjacent cells"""
        adjacent = []
        
        # Up
        if i - 1 >= 0:
            adjacent.append((i - 1, j))
        
        # Down
        if i + 1 < rows:
            adjacent.append((i + 1, j))
        
        # Left
        if j - 1 >= 0:
            adjacent.append((i, j - 1))
        
        # Right
        if j + 1 < cols:
            adjacent.append((i, j + 1))
        
        return adjacent
    
    def dfs(self, r, c, board, index, word, rows, cols, visited):
        if self.found or len(visited)>len(word):
            return
        
        if index == len(word):
            self.found = True
            return

        adj=self.getAdjacentCells(r , c, rows, cols)
        for i, j in adj:
            if (i,j) not in visited:
                if word[index] == board[i][j]:
                    visited.add((i,j))
                    self.dfs(i, j, board, index+1, word, rows, cols, visited)
                    visited.remove((i,j))



    def exist(self, board: List[List[str]], word: str) -> bool:
        self.found = False
        rows = len(board)
        cols = len(board[0])
        if rows*cols < len(word):
            return self.found
        visited=set()
        for r in range(rows):
            for c in range(cols):
                if word[0] == board[r][c]:
                    visited.add((r,c))
                    self.dfs(r, c, board, 1, word, rows, cols, visited)
                    if self.found:
                        break
                    visited.remove((r,c))

        return self.found


        