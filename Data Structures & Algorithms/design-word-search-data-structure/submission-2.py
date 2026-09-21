class Trie:
    def __init__(self):
        self.ar = [None]*26
        self.end=False


class WordDictionary:

    def __init__(self):
        self.first = Trie()

    def addWord(self, word: str) -> None:
        prev = self.first
        for ch in word:
            index=ord(ch)-97
            if prev.ar[index] is None:
                node = Trie()
                prev.ar[index]=node
            prev=prev.ar[index]
        prev.end=True
        
    def search(self, word: str) -> bool:
        return self.dfs(self.first, word)
    
    def dfs(self, prev: Trie, word:str) -> bool:
        if len(word) == 0:
            return prev.end
        ch = word[0]
        if ch == '.':
            ans = False
            for i in range(26):
                if prev.ar[i]:
                    ans = ans or self.dfs(prev.ar[i], word[1:])
            return ans
        else:
            if prev.ar[ord(ch)-97]:
                return self.dfs(prev.ar[ord(ch)-97], word[1:])
        return False
