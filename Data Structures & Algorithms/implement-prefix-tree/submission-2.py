class TreeNode:
    def __init__(self):
        self.ar = [None]*26
        self.end=False
    
    def add(self, index, node):
        self.ar[index] = node
    
    def addEnd(self):
        self.end=True
    
class PrefixTree:

    def __init__(self):
        self.first = TreeNode()

    def insert(self, word: str) -> None:
        prev=self.first
        i=0
        while i<len(word):
            if prev.ar[ord(word[i])-97] is None:
                node = TreeNode()
                prev.add(ord(word[i])-97,node)
            else:
                node = prev.ar[ord(word[i])-97]
            if i == len(word)-1:
                node.addEnd()
            #print(prev.ar[ord(word[i])-97].end, ord(word[i])-97, word[i])
            prev=node
            i+=1
            

    def search(self, word: str) -> bool:
        prev=self.first
        i=0
        while i<len(word):
            nextnode=prev.ar[ord(word[i])-97]
            if nextnode is None:
                return False
            if i == len(word)-1:
                return nextnode.end
            prev=nextnode
            #print(word[i], prev.end)
            i+=1


        

    def startsWith(self, prefix: str) -> bool:
        prev=self.first
        i=0
        while i<len(prefix):
            nextnode=prev.ar[ord(prefix[i])-97]
            if nextnode is None:
                return False
            prev=nextnode
            i+=1
        return True

        
        