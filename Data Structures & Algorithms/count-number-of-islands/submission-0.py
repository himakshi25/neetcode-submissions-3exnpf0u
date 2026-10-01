# up: [i-1][j] down: [i+1][j], left: [i][j-1] right [i][j+1]
class Solution:
    def dfs(self, grid, i, j):
        grid[i][j]=0

        if i-1>=0 and grid[i-1][j]=="1":
            self.dfs(grid, i-1, j)
        
        if i+1<len(grid) and grid[i+1][j]=="1":
            self.dfs(grid, i+1, j)
        
        if j-1>=0 and grid[i][j-1]=="1":
            self.dfs(grid, i, j-1)
        
        if j+1<len(grid[0]) and grid[i][j+1]=="1":
            self.dfs(grid, i, j+1)

    def numIslands(self, grid: List[List[str]]) -> int:
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    ans+=1
        return ans    
        