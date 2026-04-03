class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sl = len(s)
        tl = len(t)
        if (sl<tl): return ""
        ans = ""
        minc = 2000

        tm = Counter(t)
        sm = Counter("")
        l=0
        for r in range(sl):
            sm[s[r]]+=1

            while sm>=tm:
                if minc>r-l+1:
                    minc=r-l+1
                    ans = s[l:r+1]
                sm[s[l]]-=1
                if sm[s[l]] == 0:
                    sm.pop(s[l])
                l+=1

        return ans


        