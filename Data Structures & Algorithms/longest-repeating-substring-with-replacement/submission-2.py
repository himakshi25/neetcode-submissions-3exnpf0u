
# (right - left + 1) - max_freq maintain a slinding window where replacements = k, if = then shrink left, no need to change the maxfreq because at the end we only what maximum length string with that replcement which we already got once.
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        right=0
        mp = defaultdict(int)
        max_freq=0
        long_sub=0

        while right<len(s):
            mp[s[right]]+=1
            max_freq = max(max_freq,mp[s[right]])
            if (right-left+1) - max_freq > k:
                mp[s[left]]-=1
                left+=1
            else:
                long_sub = max(long_sub,right-left+1)
            right+=1
        return long_sub


        