# union, find. in parent array for every index keep their root or parent else keep its own index

class Solution:
    def find(self, x, parent)-> int: 
        if parent[x] == x:
            return x
        parent[x]= self.find(parent[x], parent)
        return parent[x]

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent=list(range(n))
        comp = n
        for e in edges:
            n1 = self.find(e[0],parent)
            n2 = self.find(e[1],parent)
            if n1!=n2:
                parent[n1]=n2
                comp-=1
            
        return comp

        