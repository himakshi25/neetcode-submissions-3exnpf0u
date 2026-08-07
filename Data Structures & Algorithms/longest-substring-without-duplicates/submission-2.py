# move right and add to set. when right already in set then move left till you find element [right]

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        long_sub=0
        st=set()
        while r<len(s):
            if s[r] in st:
                long_sub=max(long_sub,len(st))
                while l<r and s[l]!=s[r]:
                    st.remove(s[l])
                    l+=1
                l+=1
            else:
                st.add(s[r])
            r+=1
        long_sub=max(long_sub,len(st))
        return long_sub
        