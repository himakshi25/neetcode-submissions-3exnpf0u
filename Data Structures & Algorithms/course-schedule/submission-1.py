class Node:
    def __init__(self, val=-1, preq=None):
        self.val=val
        self.preq = [] if preq is None else preq

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp={}
        self.ans = None
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

        
        return self.ans if self.ans is not None else len(mp) == 0


    def dfs(self, node: Node, visited: set, mp):
        if self.ans is not None: return
        if node.val in visited:
            self.ans=False
            return
        visited.add(node.val)
        for p in node.preq:
            if p.val in mp:
                self.dfs(p, visited, mp)
        del mp[node.val]
        visited.remove(node.val)



        