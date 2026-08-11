class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        hmap = {'(':')','{':'}','[':']'}

        for c in s:
            if c in hmap:
                st.append(c)
            else:
                if st:
                    top = st.pop()
                    if hmap[top] != c:
                        return False
                else:
                    return False
        
        if not st:
            return True
        return False


        