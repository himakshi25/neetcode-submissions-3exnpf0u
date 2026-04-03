class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        s = set()
        if nums[0]>0 or nums[length-1]<0:
            return []
        for k in range(length):  
            if k-1>=0 and nums[k]==nums[k-1]:
                continue
            i=k+1
            j=length-1
            while i<j : 
                summ = nums[k] + nums[i] + nums[j]
                if summ<0:
                    i+=1
                elif summ>0:
                    j-=1
                else:
                    s.add((nums[k],nums[i],nums[j]))
                    i+=1
                    j-=1
        return [list(a) for a in s]