from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque() # rotten fruits
        rows=len(grid)
        cols=len(grid[0])
        fs=set() # track fresh fruits left in grid
        ans=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fs.add((i,j))
        q.append((-1,-1))
        while q:
            i,j = q.popleft()
            #print(i,j,len(q))
            if i==-1 and j==-1:
                if len(q)>0:
                    q.append((-1,-1))
                    ans+=1
            else:
                if i-1>=0 and grid[i-1][j]==1:
                    q.append((i-1,j))
                    grid[i-1][j]=2
                    fs.remove((i-1,j))
        
                if i+1<rows and grid[i+1][j]==1:
                    q.append((i+1,j))
                    grid[i+1][j]=2
                    fs.remove((i+1,j))
                
                if j-1>=0 and grid[i][j-1]==1:
                    q.append((i,j-1))
                    grid[i][j-1]=2
                    fs.remove((i,j-1))
                
                if j+1<cols and grid[i][j+1]==1:
                    q.append((i,j+1))
                    grid[i][j+1]=2
                    fs.remove((i,j+1))
        if fs:
            return -1
        return ans
        