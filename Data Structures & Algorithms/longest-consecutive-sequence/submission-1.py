# for every number start a forward pass to see element exist in set. To optimise it,

##we can find start point of any sequencce by checking ele-1 presence ##

# if not it means we can start forward checking now.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        pset = set(nums)
        ans=0
        for num in nums:            
            if num-1 not in pset:
                ct=1
                num+=1
                while num in pset:
                    ct+=1
                    num+=1
                ans=max(ans,ct)
        return ans