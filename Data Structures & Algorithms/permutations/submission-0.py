class Solution:
    def backtrack(self, nums, mark, result):
        if len(result) == len(nums):
            self.ans.append(result[:])

        for i in range(len(nums)):
            if mark[i] is False:
                result.append(nums[i])
                mark[i]=True
                self.backtrack(nums, mark, result)
                result.pop()
                mark[i]=False
            

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans=[]
        mark=[False]*len(nums)
        self.backtrack(nums, mark, [])
        return self.ans
        