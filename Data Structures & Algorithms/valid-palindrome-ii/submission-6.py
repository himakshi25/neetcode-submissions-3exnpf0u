class Solution:
    def ispal(self, s: str, l: int, r: int) -> bool:
        while l<r :
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True
    def validPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        while i<j and s[i] == s[j]:
            i+=1
            j-=1
        if self.ispal(s, i, j-1) or self.ispal(s, i+1, j):
            return True
        return False


