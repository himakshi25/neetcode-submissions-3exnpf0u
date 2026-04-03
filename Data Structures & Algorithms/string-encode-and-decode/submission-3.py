class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res = res+str(len(string))+"#"+string
            #print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        while i<len(s):
            #print(s[i])
            num=""
            while s[i] != "#":
                num = num + s[i]
                i+=1
            #print(num)
            length = int(num)
            res.append(s[i+1:i+1+length])
            i=i+1+length
            #print(res)
        return res
