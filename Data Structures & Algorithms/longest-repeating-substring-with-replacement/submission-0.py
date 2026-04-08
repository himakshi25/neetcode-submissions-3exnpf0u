class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ls = [0]*26
        count = -1
        i=0
        j=0
        while j<len(s) and i<=j:
            ls[ord(s[j])- ord('A')]+=1
            repl = (j-i+1)-max(ls)
            if ( repl <= k):
                count = max(j-i+1, count)
            else:
                ls[ord(s[i])- ord('A')]-=1
                i+=1
            j+=1
        
        return count
        