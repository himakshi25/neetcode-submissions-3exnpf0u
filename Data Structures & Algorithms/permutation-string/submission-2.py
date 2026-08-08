#create a counter map of string s1 O(n) and then create a sliding window of length s1 with left and right pointer and create its counter map O(n). 

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1)>len(s2)):
             return False
        if(s1==s2):
            return True
        s1mp = Counter(s1)
        left=0
        right=0
        s2mp=defaultdict(int)
        samecharcount=0
        while right<len(s2):
            if right<len(s1):
                s2mp[s2[right]]+=1
                if s2[right] in s1mp and s2mp[s2[right]] == s1mp[s2[right]]:
                    samecharcount+=1
            else:
                if samecharcount == len(s1mp):
                    return True
                if s2[left] in s1mp and s2mp[s2[left]] == s1mp[s2[left]]:
                    samecharcount-=1
                s2mp[s2[left]]-=1
                left+=1
                s2mp[s2[right]]+=1
                if s2[right] in s1mp and s2mp[s2[right]] == s1mp[s2[right]]:
                    samecharcount+=1
            right+=1
        if samecharcount == len(s1mp):
            return True
        return False
        