class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxc = 0
        
        for num in nums:
            c=1
            if num-1 in s:
                continue
            n = num+1
            while n in s:
                c+=1
                n+=1
            maxc = max(maxc,c)
        return maxc
        
        