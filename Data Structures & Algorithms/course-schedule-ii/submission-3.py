class Node:
    def __init__(self, val=-1, preq=None):
        self.val=val
        self.preq = [] if preq is None else preq

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mp={}
        self.ans = None
        self.listans=[]
        self.ansset=set()
        # create graph
        for t in prerequisites:
            af=None
            bf=None
            if t[0] in mp:
                af=mp[t[0]]
            else:
                af=Node()
                af.val=t[0]
                mp[t[0]]=af
            if t[1] in mp:
                bf=mp[t[1]]
            else:
                bf = Node()
                bf.val=t[1]
                mp[t[1]]=bf
            af.preq.append(bf)
            
        for n in range(numCourses):
            if n in mp:
                visited=set()
                self.dfs(mp[n], visited, mp)
                if self.ans is not None:
                    break
            if n not in self.ansset:
                self.listans.append(n)

        
        return self.listans if self.ans is None else []


    def dfs(self, node: Node, visited: set, mp):
        if self.ans is not None: return
        if node.val in visited:
            self.ans=False
            return
        visited.add(node.val)
        for p in node.preq:
            if p.val in mp:
                self.dfs(p, visited, mp)
        if self.ans is not None: return
        del mp[node.val]
        self.listans.append(node.val)
        self.ansset.add(node.val)
        visited.remove(node.val)
        