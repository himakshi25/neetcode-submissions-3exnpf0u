class Solution:
    def getsub(self, nums, index, result):
        if index>=len(nums):
            self.ans.add(tuple(sorted(result)))
            return
        
        self.getsub(nums, index+1, result)
        result.append(nums[index])
        self.getsub(nums, index+1, result)
        result.pop()


    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans=set()
        result=list()
        self.getsub(nums, 0, result)
        return list(self.ans)       
        