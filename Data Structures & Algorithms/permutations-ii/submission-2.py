class Solution:
    def backtrack(self, nums, mark, result):
        if len(result) == len(nums):
            self.ans.append(result[:])
            return

        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1] and mark[i-1]:
                continue
            if mark[i] is False:
                result.append(nums[i])
                mark[i]=True
                self.backtrack(nums, mark, result)
                result.pop()
                mark[i]=False
            

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.ans=[]
        mark=[False]*len(nums)
        nums=sorted(nums)
        result=[]
        self.backtrack(nums, mark, result)
        return self.ans
               