class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        minc = 2000
        for i in range(len(s)):
            m = Counter(t);
            c=0
            if s[i] in m:
                #print(s[i])
                for j in range(i, len(s)):
                    print(s[j])
                    if s[j] in m:
                        m[s[j]]-=1
                        c+=1;
                        if m[s[j]] == 0:
                            m.pop(s[j])
                    print(c)
                    if c == len(t):
                        if (j-i+1)<minc:
                            minc=j-i+1
                            ans = s[i:j+1]
                            print(f"ans: {ans}")
                            break
                print(f"count{c}")
        
        return ans


        