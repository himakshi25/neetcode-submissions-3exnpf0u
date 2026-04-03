class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = len(s);
        for i in range(l):
            s1= s[:i] + s[i+1:l]
            print(s1)
            if(s1 == s1[::-1]):
                return True
        return False