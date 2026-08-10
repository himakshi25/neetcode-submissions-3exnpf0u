#we will have 3 maps, tmap-of string t, rmap- same as t , submap - map of substring between left to right.

#vwe will find char of t which is in s and start left and right pointer from there, increment right and add char to submap and remove from repmap if present. stop right where repmap is empty, that is substring with all char of t. use small_len to save that value of length of substring. 

#now while shrinking left, first check if left element is in t and it value is > then just remove from sub_map, if value is == then add first to rep_map and remove from submap and increment left till you find ele is in t, now if map empty, take mini mini_len and if not then increment right to find element in rep_map.

# key here is check minimum twice, while after adding in right, rmap empty and after shrinking left, rmap is empty.
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s): 
            return ""
        tmap = Counter(t)
        if tmap == Counter(s):
            return s
        submap=defaultdict(int)
        rmap=Counter(t)
        ans=""
        l=0
        r=0
        min_sub = float('inf')

        while r<len(s):
            submap[s[r]]+=1
            if s[r] in rmap:
                rmap[s[r]]-=1
                if rmap[s[r]] == 0:
                    del rmap[s[r]]
            r+=1
            while not rmap:
                if r-l<min_sub:
                    min_sub=r-l
                    ans=s[l:r]
                if s[l] in tmap and submap[s[l]]==tmap[s[l]]:
                        rmap[s[l]]+=1
                else:
                    submap[s[l]]-=1
                    if submap[s[l]] == 0:
                        del submap[s[l]]
                    l+=1
        return ans
        