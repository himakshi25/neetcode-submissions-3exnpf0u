from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        rows, cols = len(grid), len(grid[0])
        for m in range(rows):
            for n in range(cols):
                q=deque()
                ct=0
                if grid[m][n] == 1:
                    q.append((m,n))
                    grid[m][n]=0
                    while q:
                        i,j=q.popleft()
                        ct+=1
                        if i-1>=0 and grid[i-1][j]==1:
                            q.append((i-1, j))
                            grid[i-1][j]=0
                        
                        if i+1<rows and grid[i+1][j]==1:
                            q.append(( i+1, j))
                            grid[i+1][j]=0
                        
                        if j-1>=0 and grid[i][j-1]==1:
                            q.append((i, j-1))
                            grid[i][j-1]=0
                        
                        if j+1<cols and grid[i][j+1]==1:
                            q.append((i, j+1))
                            grid[i][j+1]=0
                        
                ans = max(ans,ct)

        return ans
        