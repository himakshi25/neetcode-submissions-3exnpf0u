"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node is None:
            return node
        
        q=deque()
        mp={}

        q.append(node)
        start=Node(node.val)
        mp[node]=start
        while q:
            on = q.popleft()
            for nb in on.neighbors:
                if nb in mp:
                    node = mp[nb]
                else:
                    node=Node(nb.val)
                    mp[nb]=node
                    q.append(nb)
                mp[on].neighbors.append(node)
        return start
                



        
        

        