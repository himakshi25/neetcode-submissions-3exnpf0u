class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=""

        for s in strs:
            l = len(s)
            ans += str(l) + "#" + s

        return ans

    def decode(self, s: str) -> List[str]:
        ans=[]
        i=0
        d=""
        while i<len(s) :
            if s[i] == "#":
                st=""
                for j in range(int(d)):
                    i+=1;
                    st += s[i]
                ans.append(st)
                d=""
            else:
                d += s[i]
            i+=1

        return ans
