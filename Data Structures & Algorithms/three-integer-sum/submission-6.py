# this can be reduced to 2 sum and finding target. fix one element and do 2 pointer on remaining sorted array.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i, num in enumerate(nums):
            if i>0 and num == nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                val = num + nums[l] + nums[r]
                if val== 0:
                    ans.add((num,nums[l],nums[r]))
                    r-=1
                    l+=1
                elif val<0:
                    l+=1
                else:
                    r-=1
        return list(ans)



        