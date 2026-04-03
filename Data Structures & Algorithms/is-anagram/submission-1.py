class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp = defaultdict(int)
        for char in s:
            mp[char]+=1
        
        for char in t:
            if char not in mp.keys():
                return False
            mp[char]-=1
            if(mp[char] == 0):
                mp.pop(char)
        if mp != {}:
            return False
        return True
