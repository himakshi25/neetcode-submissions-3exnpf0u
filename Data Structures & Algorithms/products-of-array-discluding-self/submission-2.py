class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = [1]*l

        for i in range(1,l):
            ans[i]=ans[i-1]*nums[i-1]
        
        pr=nums[l-1]

        for j in range(l-2,-1,-1):
            ans[j]=ans[j]*pr
            pr=pr*nums[j]
            

        return ans