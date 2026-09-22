class Trie:
    def __init__(self):
        self.ar = [None]*26
        self.end = False
        self.word = None

class Solution:
    def buildTrie(self, root: Trie, words: List[str]):
        for word in words:
            prev = root
            for ch in word:
                if prev.ar[ord(ch)-97]:
                    node = prev.ar[ord(ch)-97]
                else:
                    node = Trie()
                prev.ar[ord(ch)-97] = node
                prev=node
            prev.end = True
            prev.word = word
            #print(prev.word)

    def getAdjacentCells(self, i, j, rows, cols):
        """Get indices of 4 adjacent cells"""
        adjacent = []
        
        # Up
        if i - 1 >= 0:
            adjacent.append((i - 1, j))
        
        # Down
        if i + 1 < rows:
            adjacent.append((i + 1, j))
        
        # Left
        if j - 1 >= 0:
            adjacent.append((i, j - 1))
        
        # Right
        if j + 1 < cols:
            adjacent.append((i, j + 1))
        
        return adjacent

    def startBT(self, result, board, m, n, wordnode, hashset):
        if (m,n) in hashset:
            return
        if wordnode.end and wordnode.word is not None:
            result.append(wordnode.word)
            #print(result)
            wordnode.word = None
        hashset.add((m,n))
        ls = self.getAdjacentCells(m, n, len(board), len(board[0]))
        #print(ls)
        for i, j in ls:
            ch = board[i][j]
            if wordnode.ar[ord(ch)-97]:
                #print(ch)
                self.startBT(result, board, i, j, wordnode.ar[ord(ch)-97], hashset)
        hashset.remove((m,n))


    def findResult(self, root: Trie, board: List[List[str]], result: List[str]):
        m=0
        while m < len(board):
            n=0
            while n<len(board[0]):
                ch = board[m][n]
                #print(ch)
                if root.ar[ord(ch)-97]:
                    hashset = set()
                    self.startBT(result, board, m, n, root.ar[ord(ch)-97], hashset)
                n+=1
            m+=1


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.first = Trie()
        self.buildTrie(self.first, words)
        result = []
        self.findResult(self.first, board, result)
        return result
        