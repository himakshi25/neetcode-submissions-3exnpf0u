class Node:
    def __init__(self, val, n):
        self.val=val
        self.n=n

class Solution:
    def dfs(self, node, visited):
        if node.val in visited:
            return
        visited.add(node.val)
        for nb in node.n:
            if nb not in visited:
                self.dfs(nb, visited)


    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        l = len(edges)

        if l != n-1:
            return False
        
        mp = {i: Node(i, []) for i in range(n)}
        for e in edges:
            n1=None
            n2=None
            if e[0] in mp:
                n1=mp[e[0]]
            else:
                n1=Node(e[0],[])
                mp[n1.val]=n1
            if e[1] in mp:
                n2=mp[e[1]]
            else:
                n2=Node(e[1],[])
                mp[n2.val]=n2
            n1.n.append(n2)
            n2.n.append(n1)

        
        visited=set()
        self.dfs(mp[0], visited)

        return len(visited) == n

