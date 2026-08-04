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
                l = int(d)
                ans.append(s[i+1 : i+1+l])
                i+=l
                d=""
            else:
                d += s[i]
            i+=1

        return ans
