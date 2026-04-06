class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = 0
        if len(s)==0: return maxi
        i=0
        j=0
        while i<=j and j<len(s):
            print(f"{s[j]} and {s[i:j]}")
            if s[j] in s[i:j]:
                maxi= max(j-i,maxi)
                i+=1
            else:
                j+=1
        maxi = max(j-i,maxi)
        return maxi