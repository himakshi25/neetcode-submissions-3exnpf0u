class Solution:
    def find(self, x, parent):
        if parent[x] == x:
            return x
        parent[x]=self.find(parent[x],parent)
        return parent[x]

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parent = list(range(1001))

        for e in edges:
            n1= self.find(e[0],parent)
            n2= self.find(e[1],parent)
            if n1==n2:
                return e
            else:
                parent[n1]=n2
            
        