class Solution:
    def getsub(self, nums, index, result):
        if index>=len(nums):
            self.ans.append(result[:])
            return
        
        self.getsub(nums, index+1, result)
        result.append(nums[index])
        self.getsub(nums, index+1, result)
        result.pop()


    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans=[]
        result=list()
        self.getsub(nums, 0, result)
        return self.ans
        