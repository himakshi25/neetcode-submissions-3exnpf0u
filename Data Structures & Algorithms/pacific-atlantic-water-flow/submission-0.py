from collections import deque
class Solution:
    def bfs(self, heights, m, n, s, rows, cols):
        q=deque()
        q.append((m,n))
        s.add((m,n))
        while q:
            i,j=q.popleft()
            if i-1>=0 and heights[i-1][j]>=heights[i][j]:
                if (i-1,j) not in s:
                    q.append((i-1, j))
                    s.add((i-1,j))
            
            if i+1<rows and heights[i+1][j]>=heights[i][j]:
                if (i+1,j) not in s:
                    q.append(( i+1, j))
                    s.add((i+1,j))
            
            if j-1>=0 and heights[i][j-1]>=heights[i][j]:
                
                if (i,j-1) not in s:
                    q.append((i, j-1))
                    s.add((i,j-1))
            
            if j+1<cols and heights[i][j+1]>=heights[i][j]:
                
                if (i,j+1) not in s:
                    q.append((i, j+1))
                    s.add((i,j+1))



    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows=len(heights)
        cols=len(heights[0])
        seta=set()
        setp=set()
        # pacific (r=0, all cols)
        for j in range(cols):
            self.bfs(heights, 0, j, setp, rows, cols)
        # pacific (r=all rows, c=0)
        for i in range(rows):
            self.bfs(heights, i, 0, setp, rows, cols)
        # atlantic (r=l-1, all cols)
        for j in range(cols):
            self.bfs(heights, rows-1, j, seta, rows, cols)
        # atlantic (r=all rows, c=l-1)
        for i in range(rows):
            self.bfs(heights, i, cols-1, seta, rows, cols)
        # print(setp)
        # print(seta)
        # print(setp or seta)
        # print(setp & seta)

        return list(setp & seta)

            
        