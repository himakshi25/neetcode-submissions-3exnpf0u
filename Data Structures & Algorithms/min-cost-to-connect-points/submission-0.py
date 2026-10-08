class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        num_v=len(points)
        min_cost=[float('inf')]*(num_v)
        in_tree=[False]*(num_v)
        ans=0

        min_cost[0]=0
        for i in range(num_v):
            mini_index=-1
            mini_val=float('inf')
            for j in range(num_v):
                if in_tree[j]==False and min_cost[j]<mini_val:
                    mini_val=min_cost[j]
                    mini_index=j
            #print(in_tree, mini_val)
            ans+=mini_val
            in_tree[mini_index]=True
            x,y=points[mini_index]
            for k in range(num_v):
                x1,y1=points[k]
                if in_tree[k]==False:
                    dist=abs(x1-x)+abs(y1-y)
                    min_cost[k]=min(min_cost[k], dist)
            #print(min_cost)
        
        return ans



        