class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hm = Counter(t)
        for char in s:
            if len(hm) == 0:
                return False
            if char not in hm:
                return False
            hm[char]-=1
            if hm[char]==0:
                hm.pop(char)
        if len(hm) == 0:
                return True
            
        